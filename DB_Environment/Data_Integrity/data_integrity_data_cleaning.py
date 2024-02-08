import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Support Dictionaries and List                            --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# --------------                    Data Classes                                             --------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

class Clean_Data:
    def __init__(self, df):
        """
        Initialize the Clean_Data class with a pandas DataFrame.

        :param df: pandas DataFrame to be cleaned
        """
        self.df = df

    def drop_row_if_one_or_more_null_exist(self, print_effected_records = "N"):
        """
        Drop rows with any missing values in the DataFrame.
        """
        original_count = len(self.df)
        self.df.dropna(inplace=True)
        if print_effected_records.upper() == "Y":
            print(f"...Dropped {original_count - len(self.df)} rows withat least one null value.")
            
    def drop_row_if_all_are_null(self, print_effected_records = "N"):
        """
        Drop rows with all missing values in the DataFrame.
        """
        original_count = len(self.df)
        self.df.dropna(how='all', inplace=True)
        if print_effected_records.upper() == "Y":
            print(f"...Dropped {original_count - len(self.df)} rows containing all null values.")

    def replace_missing_with_zero(self, print_effected_records = "N"):
        """
        Replace missing values in the DataFrame with 0.
        """
        missing_count = self.df.isnull().sum().sum()
        self.df.fillna(0, inplace=True)
        if print_effected_records.upper() == "Y":
            print(f"...Replaced {missing_count} missing values with zero.")
            
    def remove_duplicates(self, print_effected_records = "N"):
        """
        Remove duplicate rows from the DataFrame.
        """
        original_count = len(self.df)
        self.df.drop_duplicates(inplace=True)
        if print_effected_records.upper() == "Y":
            print(f"...Removed {original_count - len(self.df)} duplicate rows.")

    def replace_missing_with_value(self, value, field_name, print_effected_records = "N"):
        """
        Replace missing values in a specified column with a given value.

        :param value: Value to replace missing values with
        :param field_name: Column in which to replace missing values
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        missing_count = self.df[field_name].isnull().sum()
        self.df[field_name].fillna(value, inplace=True)
        if print_effected_records.upper() == "Y":
            print(f"...Replaced {missing_count} missing values in '{field_name}' with {value}.")

    def replace_missing_with_mean(self, field_name, print_effected_records = "N"):
        """
        Replace missing values in a specified numerical column with the column's mean.

        :param field_name: Column in which to replace missing values with mean
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        if not pd.api.types.is_numeric_dtype(self.df[field_name]):
            raise ValueError(f"Field '{field_name}' is not numeric and cannot use mean for replacement.")
        missing_count = self.df[field_name].isnull().sum()
        mean_value = self.df[field_name].mean()
        self.df[field_name].fillna(mean_value, inplace=True)
        if print_effected_records.upper() == "Y":
            print(f"...Replaced {missing_count} missing values in '{field_name}' with the mean value {mean_value}.")

    def convert_datatype_column(self, field_name, datatype, print_effected_records = "N"):
        """
        Convert the data type of a specified column.

        :param field_name: Column to convert
        :param datatype: Target data type
        """
        self.df[field_name] = self.df[field_name].astype(datatype)
        if print_effected_records.upper() == "Y":
            print(f"...Converted data type of '{field_name}' to {datatype}.")

    def rename_column(self, old_field_name, new_field_name, print_effected_records = "N"):
        """
        Rename a column in the DataFrame.

        :param old_field_name: Current name of the column
        :param new_field_name: New name for the column
        """
        self.df.rename(columns={old_field_name: new_field_name}, inplace=True)
        if print_effected_records.upper() == "Y":
            print(f"...Renamed column '{old_field_name}' to '{new_field_name}'.")

    def replace_inf_values(self, value, print_effected_records="N"):
        """
        Replace infinite values in the DataFrame with a specified value.

        :param value: Value to replace infinite values with
        :param print_effected_records: If 'Y', print the fields affected and the number of records affected
        """
        inf_counts = self.df.isin([np.inf, -np.inf]).sum()
        self.df.replace([np.inf, -np.inf], value, inplace=True)
        fields_eff = 0
        if print_effected_records.upper() == "Y":
            for field, count in inf_counts.items():
                if count > 0:
                    print(f"...Replaced {count} infinite values in field '{field}' with {value}.")
                    fields_eff += 1
            
            if fields_eff == 0:
                print(f"...No fields contained infinite values")

    def remove_whitespaces(self, field_name, print_effected_records = "N"):
        """
        Strip leading and trailing whitespaces from a string column.

        :param field_name: String column to remove whitespaces from
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        if not pd.api.types.is_string_dtype(self.df[field_name]) and self.df[field_name].dtype != 'object':
            raise ValueError(f"Field '{field_name}' with type {self.df[field_name].dtype} is not a string type or object type.")
        self.df[field_name] = self.df[field_name].str.strip()
        if print_effected_records.upper() == "Y":
            print(f"...Removed leading and trailing whitespaces from '{field_name}'.")

    def convert_column_lowercase(self, field_name, print_effected_records = "N"):
        """
        Convert all characters in a string column to lowercase.

        :param field_name: String column to convert to lowercase
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        self.df[field_name] = self.df[field_name].str.lower()
        if print_effected_records.upper() == "Y":
            print(f"...Converted all characters in '{field_name}' to lowercase.")

    def convert_column_uppercase(self, field_name, print_effected_records = "N"):
        """
        Convert all characters in a string column to uppercase.

        :param field_name: String column to convert to uppercase
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        self.df[field_name] = self.df[field_name].str.upper()
        if print_effected_records.upper() == "Y":
            print(f"...Converted all characters in '{field_name}' to uppercase.")

    def remove_outliers_column_threshold(self, field_name, threshold_lower, threshold_upper, print_effected_records = "N"):
        """
        Remove outliers from a numerical column based on specified lower and upper thresholds.

        :param field_name: Column from which to remove outliers
        :param threshold_lower: Lower threshold for outlier removal
        :param threshold_upper: Upper threshold for outlier removal
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        if not pd.api.types.is_numeric_dtype(self.df[field_name]):
            raise ValueError(f"Field '{field_name}' is not numeric and cannot be used for outlier removal.")
        original_count = len(self.df)
        self.df = self.df[(self.df[field_name] >= threshold_lower) & (self.df[field_name] <= threshold_upper)]
        if print_effected_records.upper() == "Y":
            print(f"...Removed {original_count - len(self.df)} outliers from '{field_name}'.")