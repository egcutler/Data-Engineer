import pandas as pd

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Support Dictionaries and List                            --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# ----
file_types = {
    ".xlsx": ["Excel Workbook", "Excel"],
    ".xls": "Excel Spreadsheet (Legacy)",
    ".docx": "Word Document",
    ".doc": "Word Document (Legacy)",
    ".pptx": "PowerPoint Presentation",
    ".ppt": "PowerPoint Presentation (Legacy)",
    ".pdf": "Portable Document Format",
    ".txt": "Text File",
    ".csv": "Comma-Separated Values",
    ".json": "JavaScript Object Notation",
    ".xml": "eXtensible Markup Language",
    ".html": "HyperText Markup Language",
    ".js": "JavaScript File",
    ".py": "Python Script",
    ".java": "Java Source File",
    ".c": "C Source File",
    ".cpp": "C++ Source File",
    ".jpg": "JPEG Image",
    ".jpeg": "JPEG Image",
    ".png": "Portable Network Graphics",
    ".gif": "Graphics Interchange Format",
    ".bmp": "Bitmap Image File",
    ".mp3": "MP3 Audio File",
    ".wav": "WAVE Audio File",
    ".mp4": "MPEG-4 Video File",
    ".avi": "Audio Video Interleave File",
    ".mov": "Apple QuickTime Movie",
    ".zip": "ZIP Archive",
    ".rar": "RAR Archive",
    ".7z": "7-Zip Archive"
}

# Mapping of file types to pandas read functions
file_types_pd = {
      'excel'                 : pd.read_excel,
      'Excel'                 : pd.read_excel,
      '.xlsx'                 : pd.read_excel,
      'xlsx'                  : pd.read_excel,
      'Comma-Separated Values': pd.read_csv,
      'JavaScript'            : pd.read_json,
      '.json'                 : pd.read_json,
      'json'                  : pd.read_json
}


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Data Classes                                             --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------


class Data_Check:

      def __init__(self, df):
            """
            Initialize the Data_Check object with a DataFrame.
            :param df: The DataFrame to be checked.
            """
            self.df = df

      def id_unique_count_thresholds(self, id_col, threshold_low_id=10, threshold_high_id=500000, \
                                     threshold_low_row=10, threshold_high_row=500000):
            """
            Check the row count and unique ID count of the DataFrame.
            Flags are raised if the counts are outside the specified thresholds.
            :param id_col: Column name of the ID in the DataFrame.
            :param threshold_low_id: Minimum threshold for distinct ID count (default 10).
            :param threshold_high_id: Maximum threshold for distinct ID count (default 500000).
            :param threshold_low_row: Minimum threshold for record (row) count (default 10).
            :param threshold_high_row: Maximum threshold for record (row) count (default 500000).
            """
            ids = self.df[id_col].tolist()
            unique_ids = set(ids)
            count_distinct_ids = len(unique_ids)
            record_count = len(ids)
            flag_count = 0

            # Check against low unique ID threshold
            if count_distinct_ids < threshold_low_id:
                  print(f'   Warning: Distinct ID count {count_distinct_ids} is below minimum threshold ({threshold_low_id})!')
                  flag_count += 1
            # Check against high unique ID threshold
            if count_distinct_ids > threshold_high_id:
                  print(f'   Warning: Distinct ID count {count_distinct_ids} is above maximum threshold ({threshold_high_id})!')
                  flag_count += 1
            # Check against high row count threshold
            if record_count > threshold_high_row:
                  print(f'   Warning: Record count {record_count} is above maximum threshold ({threshold_high_row})!')
                  flag_count += 1
            # Check against low row count threshold
            if record_count < threshold_low_row:
                  print(f'   Warning: Record count {record_count} is below minimum threshold ({threshold_low_row})!')
                  flag_count += 1
            # Passed/Failed message    
            if flag_count == 0:
                  print("...ID threshold check: Passed")
            else:
                  print(f"...{flag_count} ID threshold warnings triggered")
                  print(f"   Distinct ID count: {count_distinct_ids}")
                  print(f"   Record count: {record_count}")

      def active_ids(self, id_col, status_col, min_act_threshold=10, max_cld_threshold=500000, \
                  act_ratio_threshold=0.5, cld_ratio_threshold=0.1):
            """
            Check the ACTIVE/CLOSED account statistics in the DataFrame.
            Flags are raised if the number of active accounts is below a specified threshold
            or if the ratio of ACTIVE to CLOSED accounts falls below another specified threshold.
            :param id_col: Column name of the ID in the DataFrame.
            :param status_col: Column name of the account status (ACTIVE/CLOSED).
            :param min_act_threshold: Minimum number of active accounts threshold (default 10).
            :param max_cld_threshold: Maximum number of closed accounts threshold (default 500000).
            :param act_ratio_threshold: Minimum ratio of ACTIVE to CLOSED accounts (default 0.5).
            :param cld_ratio_threshold: Minimum ratio of CLOSED to TOTAL accounts (default 0.1).
            """
            # Creating a DataFrame with only ID and Active Columns
            df_ids = self.df[[id_col, status_col]]
            
            # Count Active and Closed IDs and calculate ratios
            active_check_list = ['ACTIVE', 'A', 'EMPLOYEED', 'E']
            closed_check_list = ['CLOSED', 'C', 'INACTIVE', 'I', 'TERMINATED', 'T']
            status_unique_values = list(set(self.df[status_col].str.upper()))

            active_value = next((val for val in status_unique_values if val in active_check_list), None)
            closed_value = next((val for val in status_unique_values if val in closed_check_list), None)

            count_id_tot = len(df_ids[status_col])
            
            if not active_value:
                  count_act_ids = 0
                  act_ratio = 0
            else:
                  count_act_ids = df_ids[status_col].str.upper().eq(active_value).sum()
                  act_ratio = count_act_ids / count_id_tot if count_id_tot != 0 else float('inf')
                  
            if not active_value:
                  count_cld_ids = 0
                  cld_ratio = 0
            else:
                  count_cld_ids = df_ids[status_col].str.upper().eq(closed_value).sum()
                  cld_ratio = count_cld_ids / count_id_tot if count_id_tot != 0 else float('inf')

            flag_count = 0
            # Check against thresholds
            if count_act_ids < min_act_threshold:
                  print(f'...Warning: Active IDs below minimum threshold ({min_act_threshold})!')
                  flag_count += 1
            if count_cld_ids > max_cld_threshold:
                  print(f'...Warning: Closed IDs above maximum threshold ({max_cld_threshold})!')
                  flag_count += 1
            if act_ratio == 0:
                  print(f'...Warning: Zero Active Type values were present!')
                  flag_count += 1
            elif act_ratio < act_ratio_threshold:
                  print(f'...Warning: Ratio of Active to Total IDs ({act_ratio:.2f}) is below threshold ({act_ratio_threshold})!')
                  flag_count += 1
            if cld_ratio == 0:
                  print(f'...Warning: Zero Closure Type values were present!')
                  flag_count += 1
            elif cld_ratio < cld_ratio_threshold:
                  print(f'...Warning: Ratio of Closed to Total IDs ({cld_ratio:.2f}) is below threshold ({cld_ratio_threshold})!')
                  flag_count += 1

            # Passed/Failed message
            if flag_count == 0:
                  print("...Active/Closed threshold checks: Passed")

      def null_check(self, null_threshold = 100):
            """
            Check for null values in the DataFrame.
            Flags fields that are entirely null.
            Flags fields where the count of null values exceeds the specified threshold.
            :param null_threshold: Threshold for the acceptable count of null values in a field.
            """
            # Check for columns that are entirely null
            all_null_columns = self.df.columns[self.df.isnull().all()]

            if len(all_null_columns) > 0:
                  print(f'...All null field check: Failed')
                  print(f'   Fields entirely null: {list(all_null_columns)}')
            else:
                  print(f'...All null field check: Passed')
            # Check for columns where null count exceeds the threshold
            flag_count = 0
            for column in self.df.columns:
                  null_count = self.df[column].isnull().sum()
                  if null_count > null_threshold:
                        print(f'   Warning: field {column} has a null count of {null_count}, exceeding threshold {null_threshold}!')
                        flag_count += 1
            if flag_count > 0:
                  print(f"...{flag_count} null column threshold warnings triggered")

      def check_duplicate_rows(self):
            """
            Identify duplicate rows in the DataFrame.
            Flags entire rows that are duplicates.
            """
            duplicates = self.df[self.df.duplicated()]
            if not duplicates.empty:
                  print("Duplicate rows found:\n", duplicates)

                  
      def check_multiple_data_types(self):
            """
            Checks each column in the DataFrame to see if it contains more than one data type.
            Prints the names of columns with multiple data types.
            """
            print_list = {}
            flag_count = 0
            for column in self.df.columns:
                  # -Get the set of unique data types for non-null values in the column
                  # -Method with dropna used to remove missing (NA/null) values from a Series or DataFrame.
                  #  Important for data type validation because missing values don't have a data type in the 
                  #  traditional sense and can lead to incorrect type checking results.
                  # -type(x) returns each data type for x iterated over each value in the data column
                  # -{} wrapping creates a set, removing all duplicates
                  unique_types = {type(x) for x in self.df[column].dropna()}

                  # Check if there is more than one unique data type
                  if len(unique_types) > 1:
                        #print(f"   Warning: column '{column}' has multiple data types {unique_types}!")
                        print_list[column] = unique_types
                        flag_count += 1
            if flag_count > 0:
                  print("...Fields with mulitple data type checks: Failed")
                  print(f"   {flag_count} fields with multiple data type warnings triggered")
                  for k, v in print_list:
                        print(f"   Warning: column '{k}' has multiple data types {v}!")
            else:
                  print(f'...Fields with multiple data types check: Passed')

      # Example of expected_type format:            
      # expected_types = {
      #     'column1 name': str,             # expecting column1 to contain strings
      #     'column2 name': int,             # expecting column2 to contain integers
      #     'column3 name': float,           # expecting column3 to contain floating point numbers
      #     'column4 name': bool,            # expecting column4 to contain boolean values
      #      etc.
      # }
      def check_explicit_data_types(self, expected_types):
            """
            Ensure that each column contains data of the expected type.
            :param expected_types: Dictionary with column names as keys and expected data types as values.
            Flags columns with unexpected data types and shows all data types present in these columns.
            """
            print_list = []
            flag_count = 0
            for column, expected_type in expected_types.items():
                  # Get the set of unique data types for non-null values in the column
                  unique_types = {type(x).__name__ for x in self.df[column].dropna()}

                  # Check if all non-null elements in the column are of the expected type
                  if not all(isinstance(x, expected_type) for x in self.df[column].dropna()):
                        # Append the column and its unique data types to the print_list
                        print_list.append((column, unique_types))
                        flag_count += 1
            
            if len(print_list) > 0:
                  print("...Fields with incorrect data type check: Failed")
                  print(f"   {flag_count} warning(s) triggered:")
                  for col, types in print_list:
                        types_str = ', '.join(sorted(types))  # Convert set of types to a sorted, comma-separated string
                        print(f"   Warning: data type issue in column {col} has data types {types_str}!")
            else:
                  print("...Fields with incorrect data type checks: Passed")     


      def check_data_len_range(self, column, min_len=0, max_len=100):
            """
            Ensure that the length of string values in a column fall within a specified length range.
            :param column: The column to check.
            :param min_len: Minimum acceptable length (inclusive).
            :param max_len: Maximum acceptable length (inclusive).
            Flags string values outside the specified length range.
            """
            string_values = self.df[column].astype(str)
            max_val = 0
            min_val = float('inf')

            # Check if any value length is outside the specified range
            if any((len(value) < min_len) or (len(value) > max_len) for value in string_values):
                  for value in string_values:
                        max_val = max(max_val, len(value))
                        min_val = min(min_val, len(value))
                  print("...Field length check: Failed")
                  print(f"   Field '{column}' has values outside the length range [{min_len}, {max_len}]")
                  print(f"   Max length value = {max_val} and Min length value = {min_val}")
            else:
                  print("...Field length check: Passed")


class Data_Check_Formats:
      def __init__(self, df):
            """
            Initialize the Data_Check_Formats object with a DataFrame.
            This class is intended for validating data formats in various fields of the DataFrame.
            :param df: The DataFrame to be validated.
            """
            self.df = df

      # Employee email address format validation
      def check_employee_email_format_field(self, column, return_list = "n"):
            """
            Validate the email address format in a specified column of the DataFrame.
            The function checks against a specified regex pattern for email validation.
            :param column: The column name containing the email addresses.
            :param return_list: Set to "y" to return a list of invalid email addresses.
            :return: Optional list of invalid email addresses if return_list is set to "y".
            """
            pattern = r"^[a-zA-Z]+\.[a-zA-Z]+\d?@mailtype\.com$"
            # Filter out NaN and empty string values before applying the regex
            filtered_df = self.df[self.df[column].notna() & (self.df[column] != '')]
            # Search for invalid zip codes based off regex pattern
            invalid_emails = filtered_df[~filtered_df[column].astype(str).str.match(pattern)][column]

            if not invalid_emails.empty:
                  # Creating a list of invalid emails
                  invalid_email_list = invalid_emails.tolist()
                  # Count of invalid emails
                  invalid_email_count = len(invalid_email_list)
                  print("...Employee email format check: Failed")
                  print(f"   {invalid_email_count} emails flagged as wrong format")
                  if return_list.lower() == "y":
                        return invalid_email_list
            else:
                  print("...Email format check: Passed")
    
      # Street address format validation
      def check_street_address_format_field(self, column, return_list="n"):
            """
            Validate the street address format in a specified column of the DataFrame.
            The function checks addresses against a regex pattern for standard street address validation.
            :param column: The column name containing street addresses.
            :param return_list: Set to "y" to return a list of invalid addresses.
            :return: Optional list of invalid addresses if return_list is set to "y".
            """
            # Define a simple street address regex pattern or use a more complex one depending on the requirement
            pattern = r"^\d+\s[A-Za-z]+(\s[A-Za-z]+)?"
            # Filter out NaN and empty string values before applying the regex
            filtered_df = self.df[self.df[column].notna() & (self.df[column] != '')]
            # Search for invalid zip codes based off regex pattern
            invalid_addresses = filtered_df[~filtered_df[column].astype(str).str.match(pattern)][column]

            if not invalid_addresses.empty:
                  # Creating a list of invalid addresses
                  invalid_address_list = invalid_addresses.tolist()
                  # Count of invalid addresses
                  invalid_address_count = len(invalid_address_list)
                  print("...Street address format check: Failed")
                  print(f"   {invalid_address_count} addresses flagged as wrong format")
                  if return_list.lower() == "y":
                        return invalid_address_list
            else:
                  print("...Street address format check: Passed")


      # Zip Code format validation (5 or 9 digit)
      def check_zip_code_format_field(self, column, return_list="n"):
            """
            Validate the zip code format in a specified column of the DataFrame.
            The function checks zip codes against a regex pattern for standard 5 or 9 digit zip code validation.
            It excludes NaN and empty string values.
            :param column: The column name containing zip codes.
            :param return_list: Set to "y" to return a list of invalid zip codes.
            :return: Optional list of invalid zip codes if return_list is set to "y".
            """
            pattern = r"^\d{5}(-\d{4})?$"
            # Filter out NaN and empty string values before applying the regex
            filtered_df = self.df[self.df[column].notna() & (self.df[column] != '')]
            # Search for invalid zip codes based off regex pattern
            invalid_zip_codes = filtered_df[~filtered_df[column].astype(str).str.match(pattern)][column]

            if not invalid_zip_codes.empty:
                  invalid_zip_code_list = invalid_zip_codes.tolist()
                  print("...Zip code format check: Failed")
                  print(f"   {len(invalid_zip_code_list)} zip code(s) flagged as wrong format")
                  if return_list.lower() == "y":
                        return invalid_zip_code_list
            else:
                  print("...Zip code format check: Passed")

      # IP address format validation
      def check_ip_address_format_field(self, column, return_list="n"):
            """
            Validate the IP address format in a specified column of the DataFrame.
            The function checks IP addresses against a regex pattern for standard IP address validation.
            :param column: The column name containing IP addresses.
            :param return_list: Set to "y" to return a list of invalid IP addresses.
            :return: Optional list of invalid IP addresses if return_list is set to "y".
            """
            pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
            # Filter out NaN and empty string values before applying the regex
            filtered_df = self.df[self.df[column].notna() & (self.df[column] != '')]
            # Search for invalid zip codes based off regex pattern
            invalid_ips = filtered_df[~filtered_df[column].astype(str).str.match(pattern)][column]
            
            if not invalid_ips.empty:
                  invalid_ip_list = invalid_ips.tolist()
                  print("...IP address format check: Failed")
                  print(f"   {len(invalid_ip_list)} IP addresses flagged as wrong format")
                  if return_list.lower() == "y":
                        return invalid_ip_list
            else:
                  print("...IP address format check: Passed")

      # Domain name (website) format validation
      def check_domain_name_format_field(self, column, return_list="n"):
            """
            Validate the domain name format in a specified column of the DataFrame.
            The function checks domain names against a regex pattern for standard domain name validation.
            :param column: The column name containing domain names.
            :param return_list: Set to "y" to return a list of invalid domain names.
            :return: Optional list of invalid domain names if return_list is set to "y".
            """
            pattern = r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
            # Filter out NaN and empty string values before applying the regex
            filtered_df = self.df[self.df[column].notna() & (self.df[column] != '')]
            # Search for invalid zip codes based off regex pattern
            invalid_domains = filtered_df[~filtered_df[column].astype(str).str.match(pattern)][column]
            
            if not invalid_domains.empty:
                  invalid_domain_list = invalid_domains.tolist()
                  print("...Domain name format check: Failed")
                  print(f"   {len(invalid_domain_list)} domain names flagged as wrong format")
                  if return_list.lower() == "y":
                        return invalid_domain_list
            else:
                  print("...Domain name format check: Passed")

      def validate_against_reference(self, column, reference_data):
            """
            Validate the entries of a specified column against a set of reference data.
            Flags entries in the column that are not found in the reference data.
            :param column: The column name to be validated.
            :param reference_data: The set of reference data to validate against.
            """
            if not set(self.df[column]).issubset(set(reference_data)):
                  print(f"Reference data issue in column: {column}")
                  
# This class and its functions are still under construction
class Data_Check_Time_Series:
      """
      Initialize the Data_Check_Time_Series object with a DataFrame.
      Intended for analyzing time series data within the DataFrame.
      :param df: The DataFrame to be analyzed.
      """
      def __init__(self, df):
            self.df = df

      def analyze_time_series(self, time_column):
            """
            Check for anomalies in time-series data.
            This function is currently under construction.
            :param time_column: The column containing time-series data.
            """
            pass

# This class and its functions are still under construction
class Data_Check_Correlations:
      """
      Initialize the Data_Check_Correlations object with a DataFrame.
      Intended for identifying unexpected correlations between columns in the DataFrame.
      :param df: The DataFrame to be analyzed.
      """
      def __init__(self, df):
            self.df = df
            
      def analyze_correlation(self):
            """
            Identify unexpected correlations between columns.
            This function is currently under construction and will compute and print the correlation matrix of the DataFrame.
            """
            pass
            #correlation_matrix = self.df.corr()
            #print(correlation_matrix)
            
