import pandas as pd
import random
from datetime import datetime, timedelta
import generate_random_dataset_support_functions as gtsf

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Address List for Support Functions              ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Address (street line, city, state and country) Components for random generator
street_names = [
    "Maple", "Oak", "Pine", "Cedar", "Elm", "Willow", "Peach", "Cherry", 
    "Magnolia", "Walnut", "Poplar", "Aspen", "Birch", "Spruce", "Hickory",
    "Sycamore", "Chestnut", "Laurel", "Redwood", "Sequoia", "Cypress"
]
city_names = [
    "Springfield", "Rivertown", "Meadowville", "Eaglewood", "Sunnyvale", 
    "Greenfield", "Kingsport", "Fairview", "Lakeview", "Ridgecrest", "Westbrook",
    "Easton", "Harborview", "Brookfield", "Cliffside", "Rockville", "Mapleton",
    "Hilltop", "Lakeside", "Rainbow City", "Sunset Hills"
]
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
    "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
    "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
    "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
    "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

country_abbreviations = [
      'US', 'UK', 'CAN', 'AUS', 'GER', 'FRA', 'JPN', 'CHN', 'RUS', 'BRA', 'IND'
]

addr_abbr_dict = {
    'Road': 'Rd',
    'Street': ['Str', 'St'],
    'Avenue': 'Ave',
    'Boulevard': 'Blvd',
    'Drive': 'Dr',
    'Court': 'Ct',
    'Lane': 'Ln',
    'Terrace': 'Ter',
    'Place': 'Pl',
    'Square': 'Sq',
    'Trail': 'Trl',
    'Parkway': 'Pkwy',
    'Alley': 'Aly',
    'Center': 'Ctr',
    'Crossing': 'Xing',
    'Loop': 'Lp'
}

addr_street_type_list = [
    'Road',
    'Street',
    'Avenue',
    'Boulevard',
    'Drive',
    'Court',
    'Lane',
    'Terrace',
    'Place',
    'Circle',
    'Highway',
    'Square',
    'Trail',
    'Parkway',
    'Alley',
    'Center',
    'Mill',
    'Gardens'
    'Crescent',
    'Crossing',
    'Loop'
]

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Address Support Functions                       ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Function to generate a random address
def generate_random_address(street_names, city_names, states):
      """
      Generate a random address.
      :param street_names: List of possible street names.
      :param city_names: List of possible city names.
      :param states: List of possible states.
      :return: A string representing a random address.
      """
      street_name = random.choice(street_names)
      street_type = random.choice(addr_street_type_list)
      city_name = random.choice(city_names)
      state = random.choice(states)
      street_number = random.randint(100, 9999)
      zip_cond = random.randint(1,2)
      if zip_cond == 1:
            zip_code = str(f"{random.randint(10000, 99999)}")
      else:    
            zip_code = str(f"{random.randint(10000, 99999)}-{random.randint(1000, 9999)}")
            
      return f"{street_number} {street_name} {street_type}, {city_name}, {state}, {zip_code}"

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Address Functions for Generator                 ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Generate the Address Account field
def generate_address_account_field(num_records, len_id_char = 8):
      """
      Generate a list of random integers representing address account fields.
      :param num_records: Number of records to generate.
      :param len_id_char: Length of each integer in characters (default is 8).
      :return: List of random integers representing address accounts.
      """
      dict_list = []
      if type(len_id_char) == str:
            if len_id_char.isdigit():
                  zeros_req = int(len_id_char)-1
            else:
                  return Exception(f'Cannot convert the numeric string to a numeric value: {len_id_char}')
      else:
            zeros_req = len_id_char - 1
            
      zeros = "0" * zeros_req
      min = int("1"+zeros)
      max = int("9"*len_id_char) 
      for _ in range(num_records):
            dict_list.append(random.randint(min, max))
      return dict_list

# Generate the Address line fields
def generate_address_fields(num_records):
      """
      Generate address components for a specified number of records.
      :param num_records: Number of records to generate address components for.
      :return: Four lists containing address street, city, state, and zipcode.
      """
      dict_addr_street_list = []
      dict_addr_city_list = []
      dict_addr_state_list = []
      dict_addr_zipcode_list = []
  
      for _ in range(num_records):
            addr = generate_random_address(street_names, city_names, states).split(", ")
            dict_addr_street_list.append(addr[0])
            dict_addr_city_list.append(addr[1])
            dict_addr_state_list.append(addr[2])
            dict_addr_zipcode_list.append(addr[3])
      return dict_addr_street_list, dict_addr_city_list, dict_addr_state_list, dict_addr_zipcode_list

# Generate the Address Original Country field
def generate_address_original_country_field(num_records, priority_item = 'US', weight_us = 10, weight_oth = 1):
      """
      Generate a list of country abbreviations with a weighted priority for a specific country.
      :param num_records: Number of records to generate.
      :param priority_item: Country abbreviation to prioritize (default 'US').
      :param weight_us: Weight for the priority country (default 10).
      :param weight_oth: Weight for other countries (default 1).
      :return: List of country abbreviations.
      """
      dict_list = [] 
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_unique_weighted_list(country_abbreviations, priority_item, weight_us, weight_oth))
      return dict_list
     
# Generate the Address Registered Country field 
def generate_address_registered_country_field(num_records):
      """
      Generate a list of 'US' country abbreviations for a specified number of records.
      :param num_records: Number of records to generate.
      :return: List of 'US' country abbreviations.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append('US')
      return dict_list

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Address Table                      ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Function to run each field to build the address table
def generate_table_address_general(dict, id_field_name = 'ID_Record'):
      """
      Build an address table by generating various address-related fields.
      :param dict: Dictionary to populate with address data.
      :param num_records: Number of records to generate for the table.
      :return: Dictionary populated with generated address data.
      """
      num_records = len(dict[id_field_name])
      dict['Address ID'] = generate_address_account_field(num_records)
      dict['Address Street'], dict['City'], dict['State'], dict['Zip Code'] = generate_address_fields(num_records)
      dict['Registered Country'] = generate_address_registered_country_field(num_records)
      dict['Original Country'] = generate_address_original_country_field(num_records, weight_us=20)
      return dict

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

# # Main function to run the address table generator
# def generate_table_address(min_rand_record_lim = 1, max_rand_record_lim = 100000):
#       """
#       Generate a table of addresses with random data.
#       :param min_rand_record_lim: Minimum limit for random record length (default 1).
#       :param max_rand_record_lim: Maximum limit for random record length (default 100000).
#       :return: Dictionary representing the generated address table.
#       """
#       addr_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
#       addr_data = gtsf.table_generate_id_records(addr_num_records)
#       addr_data = generate_table_address_build(addr_data, addr_num_records)
#       return addr_data
