import pandas as pd
import random
from generate_random_dataset_address import addr_abbr_dict
import generate_random_dataset_support_functions as grdsf
import datetime
import re

class Data_Analysis_Inserts:
      """
      This class provides methods for inserting specific types of data alterations into a pandas DataFrame. 
      It includes functions to create duplicates within a field and insert specific values into a DataFrame.
      """
      def __init__(self, df):
            """
            Initialize the Data_Analysis_Inserts object with a DataFrame.
            :param df: The DataFrame to be manipulated.
            """
            self.df = df

      def create_duplicates_within_field_random(self, field_name, dup_option_perc = random.randint(10,30), field_perc_to_dup = random.randint(10,30)):
            """
            Create duplicates within a specified field in the DataFrame.
            :param field_name: The name of the field where duplicates are to be created.
            :param dup_option_perc: Percentage of unique values to be duplicated (default random 10-30%).
            :param field_perc_to_dup: Percentage of the field to be duplicated (default random 10-30%).
            """
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if dup_option_perc > 100 or dup_option_perc < 0.1:
                  raise Exception(f"dup_option_perc value of {dup_option_perc} is not between 0.1% - 100%")
            if field_perc_to_dup > 100 or field_perc_to_dup < 0.1:
                  raise Exception(f"field_perc_to_dup value of {field_perc_to_dup} is not between 0.1% - 100%")
            
            # Duplication option
            unique_values = list(set(self.df[field_name]))
            duplication_option_perc_num = round(len(unique_values) * (dup_option_perc/100))
            values_to_duplicate = random.sample(unique_values, duplication_option_perc_num)
            
            # Override values at the selected positions with the duplicated values
            duplication_field_perc_num = round(len(self.df[field_name]) * (field_perc_to_dup/100))
            index_positions_to_override = random.sample(range(len(self.df)), duplication_field_perc_num)
            for index in index_positions_to_override:
                  self.df.at[index, field_name] = random.choice(values_to_duplicate)
            return self.df

      
      def insert_value_by_override_perc(self, field_name, field_perc_to_dup = random.randint(10,20), value = ""):
            """
            Insert a specific value into a field by overriding a percentage of its values.
            :param field_name: The name of the field to be modified.
            :param field_perc_to_dup: Percentage of the field to be overridden (default random 10-20%).
            :param value: The value to be inserted (default empty).
            """
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if field_perc_to_dup > 100 or field_perc_to_dup < 0.1:
                  raise Exception(f"field_perc_to_dup value of {field_perc_to_dup} is not between 0.1% - 100%")
            
            # Override values at the selected positions with Null
            duplication_field_perc_num = round(len(self.df[field_name]) * (field_perc_to_dup/100))
            index_positions_to_override = random.sample(range(len(self.df)), duplication_field_perc_num)
            for index in index_positions_to_override:
                  self.df.at[index, field_name] = value
            return self.df
            
      

class Data_Analysis_Changes:
      def __init__(self, df):
            self.df = df
            
      def target_value_change_value(self, field_name, field_perc_to_dup = random.randint(10,20), target_value="", change_value = ""):
            if field_perc_to_dup is None:
                  field_perc_to_dup = random.randint(10, 20)
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if field_perc_to_dup > 100 or field_perc_to_dup < 0.1:
                  raise Exception(f"field_perc_to_dup value of {field_perc_to_dup} is not between 0.1% - 100%")
            
            # Generate index list for each record the targeted value occurs
            index_loc = []  
            for index in range(len(self.df)):
                  if target_value.lower() in self.df.at[index, field_name].lower():
                        index_loc.append(index)
            
            # Apply the percentage operator on the index list
            random.shuffle(index_loc)
            duplication_field_perc_num = round(len(index_loc) * (field_perc_to_dup/100))  
            index_positions_to_override = index_loc[:duplication_field_perc_num]
            # Remove duplicates
            index_positions_to_override = list(set(index_positions_to_override))
            # Override targeted values at the percentaged index positions with the change value
            for index in index_positions_to_override:
                  self.df.at[index, field_name] = self.df.at[index, field_name].replace(target_value, change_value)
            return self.df
      
      def not_target_record_change_record(self, field_name, field_perc_to_dup = random.randint(10,20), not_target_record="", change_record = ""):
            if field_perc_to_dup is None:
                  field_perc_to_dup = random.randint(10, 20)
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if field_perc_to_dup > 100 or field_perc_to_dup < 0.1:
                  raise Exception(f"field_perc_to_dup value of {field_perc_to_dup} is not between 0.1% - 100%")
            
            # Generate index list for each record the targeted value occurs
            index_loc = []  
            for index in range(len(self.df)):
                  if not_target_record.lower() not in self.df.at[index, field_name].lower():
                        index_loc.append(index)

            # Apply the percentage operator on the index list
            random.shuffle(index_loc)
            duplication_field_perc_num = round(len(index_loc) * (field_perc_to_dup/100))  
            index_positions_to_override = index_loc[:duplication_field_perc_num]
            # Remove duplicates
            index_positions_to_override = list(set(index_positions_to_override))
            # Override targeted values at the percentaged index positions with the change value
            for index in index_positions_to_override:
                  self.df.at[index, field_name] = change_record
            return self.df
      
      def target_records_change_record_diff_fields(self, target_field1, target_value1, change_field, change_value,\
                                                         target_field2 = "-----", target_value2 = "-----", \
                                                         target_field3 = "-----", target_value3 = "-----", \
                                                         target_field4 = "-----", target_value4 = "-----", \
                                                         field_perc_to_dup = random.randint(10,20)):
            # Required argument checks  
            if field_perc_to_dup is None:
                  field_perc_to_dup = random.randint(10, 20)
            if target_field1 not in self.df.columns:
                  raise ValueError(f"{target_field1} not in DataFrame")
            if change_field not in self.df.columns:
                  raise ValueError(f"{change_field} not in DataFrame")
            if not isinstance(change_value, self.df[change_field].dtype.type):
                  #raise ValueError(f"Data type of change value {type(change_value)} does not match the data type for field '{change_field}', which is {self.df[change_field].dtype}")
                  pass
            # Potential argument checks        
            if target_field2 != "-----" and target_field2 not in self.df.columns:
                  raise ValueError(f"{target_field2} not in DataFrame")
            if target_field3 != "-----" and target_field3 not in self.df.columns:
                  raise ValueError(f"{target_field3} not in DataFrame")
            if target_field4 != "-----" and target_field4 not in self.df.columns:
                  raise ValueError(f"{target_field4} not in DataFrame")
            if target_field2 == "-----" and target_field3 != "-----" and target_field4 != "-----":
                  raise ValueError(f"Target fields 1 '{target_field1}', 3 '{target_field3}', and 4 '{target_field4}' were entered, however Target Field 2 is missing")
            if target_field2 != "-----" and target_field3 == "-----" and target_field4 != "-----":
                  raise ValueError(f"Target fields 1 '{target_field1}', 2 '{target_field2}', and 4 '{target_field4}' were entered, however Target Field 3 is missing")
            if target_field2 == "-----" and target_field3 == "-----" and target_field4 != "-----":
                  raise ValueError(f"Target fields 1 '{target_field1}' and 4 '{target_field4}' were entered, however Target Field 2 and 3 are missing")

            # Determine case
            if target_field4 == "-----":
                  if target_field3 == "-----":
                        if target_field2 == "-----":
                              case_degree = 1
                        else:
                              case_degree = 2
                  else:
                        case_degree = 3
            else:
                  case_degree = 4
            
            # Generate index list for each record the targeted value occurs
            index_loc = [] 
            if case_degree == 4: 
                  for index in range(len(self.df)):
                        if target_value1.lower() in self.df.at[index, target_field1].lower() and \
                           target_value2.lower() in self.df.at[index, target_field2].lower() and \
                           target_value3.lower() in self.df.at[index, target_field3].lower() and \
                           target_value4.lower() in self.df.at[index, target_field4].lower():
                              index_loc.append(index) 
            elif case_degree == 3:
                  for index in range(len(self.df)):
                        if target_value1.lower() in self.df.at[index, target_field1].lower() and \
                           target_value2.lower() in self.df.at[index, target_field2].lower() and \
                           target_value3.lower() in self.df.at[index, target_field3].lower():
                              index_loc.append(index)
            elif case_degree == 2:
                  for index in range(len(self.df)):
                        if target_value1.lower() in self.df.at[index, target_field1].lower() and \
                           target_value2.lower() in self.df.at[index, target_field2].lower():
                              index_loc.append(index)
            else:
                  for index in range(len(self.df)):
                        if target_value1.lower() in self.df.at[index, target_field1].lower():
                              index_loc.append(index)
            # Apply the percentage operator on the index list
            random.shuffle(index_loc)
            duplication_field_perc_num = round(len(index_loc) * (field_perc_to_dup/100))  
            index_positions_to_override = index_loc[:duplication_field_perc_num]
            # Override change field at the percentaged index positions with the change value
            for index in index_positions_to_override:
                  self.df.at[index, change_field] = change_value
            return self.df
            
      def address_abbreviation_change(self, field_name, field_perc_to_dup = random.randint(10,20)):
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if field_perc_to_dup > 100 or field_perc_to_dup < 0.1:
                  raise Exception(f"field_perc_to_dup value of {field_perc_to_dup} is not between 0.1% - 100%")
            
            index_loc = []
            addr_list = list(addr_abbr_dict.keys())
            addr_list = [value.lower() for value in addr_list]
            for index in range(len(self.df)):
                  df_value = self.df.at[index, field_name].lower()
                  for addr_type in addr_list:
                        if addr_type in df_value:
                              index_loc.append(index)
            
            # Override values at the selected positions with address abbreviations
            random.shuffle(index_loc)
            duplication_field_perc_num = round(len(index_loc) * (field_perc_to_dup/100))
            index_positions_to_override = index_loc[:duplication_field_perc_num]
            index_positions_to_override = list(set(index_positions_to_override))
            for index in index_positions_to_override:
                  original_value = self.df.at[index, field_name]
                  for full, abbr in addr_abbr_dict.items():
                        # If abbreviation is a list, choose the first one or randomly
                        abbr_value = abbr[0] if isinstance(abbr, list) else abbr
                        # Replace with abbreviation (both lowercase for case-insensitive matching)
                        self.df.at[index, field_name] = original_value.lower().replace(full.lower(), abbr_value.lower())
                        original_value = self.df.at[index, field_name]
                  self.df.at[index, field_name] = self.df.at[index, field_name].title()
                  
            return self.df
            
      
class Data_Analysis_Err_Conditions:
      def __init__(self, df):
            self.df = df
      
      def closed_date_misalignment(self, closed_date_field, open_date_field=None, modified_date_field=None, apply_perc=None, cond_between_open_mod="Y"):
            if apply_perc is None:
                  apply_perc = random.randint(10, 20)
            if not (0.1 <= apply_perc <= 100):
                        raise ValueError(f"apply_perc value of {apply_perc} is not between 0.1% - 100%")
            date_fields = []
            for field in [open_date_field, closed_date_field, modified_date_field]:
                  if field not in self.df.columns and field != None and field != "":
                        raise ValueError(f"{field} not in DataFrame")
                  if field == open_date_field and field != None and field != "":
                        date_fields.append(open_date_field)     
                  if field == modified_date_field and field != None and field != "":
                        date_fields.append(modified_date_field)
            # Determine the earliest date to be used as the start date
            min_date = self.df[date_fields].min().min()
            # Check if the result is NaT (Not a Time) or pd.isnull(min_dates) to handle both NaT and None
            if pd.isnull(min_date):
                  min_date = pd.to_datetime(datetime.date.today())
            else:
                  min_date = pd.to_datetime(min_date)

            # Calculate the number of records to modify
            num_records_to_modify = round(len(self.df) * (apply_perc / 100))
            # Select random indices to modify
            indices_to_modify = random.sample(range(len(self.df)), num_records_to_modify)
            
            open_case = 0
            mod_case = 0
            if open_date_field != "" and open_date_field != None:
                  open_case = 1
            if modified_date_field != "" and modified_date_field != None:
                  mod_case = 1
            for index in indices_to_modify:      
                  start_date = min_date
                  if open_case == 1 and mod_case == 1:
                        # Prep df index iff argument conditions
                        open_val_case = 0
                        mod_val_case = 0
                        if self.df.at[index, open_date_field] != "" and not pd.isna(self.df.at[index, open_date_field]) and self.df.at[index, open_date_field] != pd.NaT: 
                              open_val_case = 1
                        if self.df.at[index, modified_date_field] != "" and not pd.isna(self.df.at[index, modified_date_field]) and self.df.at[index, modified_date_field] != pd.NaT: 
                              mod_val_case = 1
                        # Prepare end date
                        # (only for first iff condition: modify start date to be between open date field and modified date field)
                        if cond_between_open_mod == "Y" and open_val_case == 1 and mod_val_case == 1: 
                              start_date = pd.to_datetime(self.df.at[index, open_date_field])
                              end_date = pd.to_datetime(self.df.at[index, modified_date_field])
                        elif open_val_case == 1 and mod_val_case == 1:
                              end_date = pd.to_datetime(self.df.at[index, modified_date_field or open_date_field])
                        elif open_val_case == 0 and mod_val_case == 1:
                              end_date = pd.to_datetime(self.df.at[index, modified_date_field])
                        else:
                              end_date = pd.to_datetime(self.df.at[index, open_date_field])
                        
                        # Correcting equal dates condition   
                        if start_date == end_date:
                              start_date = start_date - pd.Timedelta(days=10)   
                        generated_date = grdsf.random_date(start_date, end_date)
                         # Convert the generated date to datetime64[ns] type
                        compatible_date = pd.to_datetime(generated_date)
                        # Assign the converted date to the DataFrame
                        self.df.at[index, closed_date_field] = compatible_date
                        #self.df.at[index, closed_date_field] = grdsf.random_date(start_date, end_date)
                        
                  elif open_case == 1 and mod_case != 1:
                        # Check if open date record is populated
                        open_val_case = 0
                        if self.df.at[index, open_date_field] != "" and not pd.isna(self.df.at[index, open_date_field]) and self.df.at[index, open_date_field] != pd.NaT: 
                              open_val_case = 1
                        # Generate end date
                        if open_val_case == 1:      
                              end_date = pd.to_datetime(self.df.at[index, open_date_field])
                        else:
                              end_date = datetime.date.today()
                        
                        # Generate the random date    
                        if start_date == end_date:
                              start_date = start_date - pd.Timedelta(days=10)
                              
                        generated_date = grdsf.random_date(start_date, end_date)
                         # Convert the generated date to datetime64[ns] type
                        compatible_date = pd.to_datetime(generated_date)
                        # Assign the converted date to the DataFrame
                        self.df.at[index, closed_date_field] = compatible_date
                        #self.df.at[index, closed_date_field] = grdsf.random_date(start_date, end_date)
                  elif open_case != 1 and mod_case == 1:
                        # Check if open date record is populated
                        open_val_case = 0
                        if self.df.at[index, modified_date_field] != "" and not pd.isna(self.df.at[index, modified_date_field]) and self.df.at[index, modified_date_field] != pd.NaT: 
                              open_val_case = 1
                        # Generate end date
                        if open_val_case == 1:      
                              end_date = pd.to_datetime(self.df.at[index, modified_date_field])
                        else:
                              end_date = datetime.date.today()
                              
                        # Generate the random date    
                        if start_date == end_date:
                              start_date = start_date - pd.Timedelta(days=10)
                              
                        generated_date = grdsf.random_date(start_date, end_date)
                         # Convert the generated date to datetime64[ns] type
                        compatible_date = pd.to_datetime(generated_date)
                        # Assign the converted date to the DataFrame
                        self.df.at[index, closed_date_field] = compatible_date
                        #self.df.at[index, closed_date_field] = grdsf.random_date(start_date, end_date)
                  else:
                        end_date = datetime.date.today()
                        # Generate the random date    
                        generated_date = grdsf.random_date(start_date, end_date)
                         # Convert the generated date to datetime64[ns] type
                        compatible_date = pd.to_datetime(generated_date)
                        # Assign the converted date to the DataFrame
                        self.df.at[index, closed_date_field] = compatible_date
                        #self.df.at[index, closed_date_field] = grdsf.random_date(start_date, end_date)
            return self.df
      
      def address_incorrect_format(self, field_name, apply_perc=None):
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if apply_perc is None:
                  apply_perc = random.randint(10, 20)
            if not (0.1 <= apply_perc <= 100):
                        raise ValueError(f"apply_perc value of {apply_perc} is not between 0.1% - 100%")
            

            indexes = self.df.index[self.df[field_name].notnull()].tolist()
            num_records_to_modify = round(len(indexes) * (apply_perc / 100))
            # Ensure that num_records_to_modify is not greater than the length of indexes
            num_records_to_modify = min(num_records_to_modify, len(indexes))
            # Select random indices to modify
            indices_to_modify = random.sample(indexes, num_records_to_modify)

            pattern = r'^\d+\s[A-Za-z\s]+$'
            for index in indices_to_modify:
                  # Check if variable is in basic street format
                  if not re.match(pattern, self.df.at[index, field_name]):
                        pass
                  else:
                        addr_err_code = random.randint(1,2)
                        if addr_err_code == 1:
                              # Regular expression to find the digit part of the address, and replace it with only the first digit
                              # ^\d+\s* matches the beginning of the string, one or more digits, followed by zero or more spaces
                              match = re.search(r'^\d+', self.df.at[index, field_name])
                              street_number = match.group()
                              shortened_street_number = street_number[:1]
                              self.df.at[index, field_name] = re.sub(r'^\d+', shortened_street_number, self.df.at[index, field_name])
                        elif addr_err_code == 2:
                              # Regular expression to remove the numeric part at the beginning of the address
                              # ^\d+\s* matches the beginning of the string, one or more digits, followed by zero or more spaces
                              self.df.at[index, field_name] = re.sub(r'^\d+\s*', '', self.df.at[index, field_name])
                        else:
                              pass
            
            return self.df
                  
            
      
      def email_incorrect_format(self, field_name, apply_perc=None):
            if field_name not in self.df.columns:
                  raise ValueError(f"{field_name} not in DataFrame")
            if apply_perc is None:
                  apply_perc = random.randint(10, 20)
            if not (0.1 <= apply_perc <= 100):
                        raise ValueError(f"apply_perc value of {apply_perc} is not between 0.1% - 100%")
            
            indexes = self.df.index[self.df[field_name].notnull()].tolist()
            num_records_to_modify = round(len(indexes) * (apply_perc / 100))
            # Ensure that num_records_to_modify is not greater than the length of indexes
            num_records_to_modify = min(num_records_to_modify, len(indexes))
            # Select random indices to modify
            indices_to_modify = random.sample(indexes, num_records_to_modify)
            
            pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            for index in indices_to_modify:
                  # Check if variable is in basic street format
                  if not re.match(pattern, self.df.at[index, field_name]):
                        pass
                  else:
                        err_code = random.randint(1, 4)
                        email = self.df.at[index, field_name]
                        if err_code == 1:
                              # remove .com
                              self.df.at[index, field_name] = email.replace('.com', '')
                        elif err_code == 2:
                              # remove @
                              self.df.at[index, field_name] = email.replace('@', '')
                        elif err_code == 3:
                              # remove everything after @
                              at_index = email.find('@')
                              if at_index != -1:
                                    self.df.at[index, field_name] = email[:at_index]
                        else:
                              # remove everything before @
                              at_index = email.find('@')
                              if at_index != -1:
                                    self.df.at[index, field_name] = email[at_index+1:]
                                    
            return self.df