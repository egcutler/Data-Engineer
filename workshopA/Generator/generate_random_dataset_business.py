import pandas as pd
import random
from datetime import datetime, timedelta
import generate_random_dataset_support_functions as gtsf

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Business List for Support Functions              ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Business names (adjectives, nouns and keywords) list for random generator
bus_list_adjectives = [
    "Acme", "Apex", "Global", "Infinite", "Dynamic", "Epic", "Swift", "Mega", 
    "Prime", "Tech", "Fusion", "Alpha", "Omega", "Brilliant", "Vibrant", 
    "Ultimate", "Superior", "Elite", "Innovative", "Creative", "Excellent", 
    "Proactive", "Strategic", "Diverse", "Flexible", "Pioneer", "Visionary"
]
bus_list_nouns = [
    "Solutions", "Systems", "Enterprises", "Innovations", "Industries", 
    "Services", "Technologies", "Ventures", "Group", "Labs", "Corp", "Co", 
    "Networks", "Enterprises", "Enterprises", "Consulting", "Solutions", 
    "Dynamics", "Solutions", "Solutions", "Technologies", "Group", "Innovations", 
    "Enterprises", "Enterprises", "Enterprises", "Consulting"
]
bus_list_keywords = [
    "Advanced", "Digital", "Tech", "Innovative", "Global", "Sustainable", 
    "Creative", "Power", "Future", "Precision", "First", "Smart", "Synergy", 
    "Synergistic", "Strategic", "Revolutionary", "Cutting-Edge", "Dynamic", 
    "Dynamic", "Ingenious", "Transformative", "Inspire", "Inspiration", "Progressive", 
    "Evolve", "Evolution", "Impactful", "Forward", "Strive", "Strive", "Vision", "Visionary"
]

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Business Functions for Generator                ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Generate the Business Account field
def generate_account_field(dict_list_id, num_records):
      """
      Generate a list of formatted account numbers based on a list of IDs and total number of records.
      :param dict_list_id: List of unique identifiers.
      :param num_records: Total number of records.
      :return: List of formatted account numbers.
      """
      dict_list = []
      # Generating the Account Column
      for x in dict_list_id:
            zero_count = len(str(num_records)) - len(str(x))
            if zero_count == 0:
                  dict_list.append(str(x))
            else: 
                  zero_addon = '0' * zero_count
                  dict_list.append(zero_addon + str(x))
      return dict_list

# Generate the Business Branch field
def generate_random_branch_field(num_records):
      """
      Generate a list of random branch identifiers for a specified number of records.
      :param num_records: Number of branch identifiers to generate.
      :return: List of branch identifiers.
      """
      dict_list = []
      # Generating the Account Column
      for _ in range(num_records):
            dict_list.append( str(gtsf.generate_random_int(0,9)) + gtsf.generate_random_letter(3) )
      return dict_list

# Generate the Business Status field
def generate_random_status_field(num_records, weightAct = 60, weightCls = 10, weightHis = 10):
      """
      Generate a list of random business statuses with specified weighting.
      :param num_records: Number of statuses to generate.
      :param weightAct: Weight for 'ACTIVE' status.
      :param weightCls: Weight for 'CLOSED' status.
      :param weightHis: Weight for 'HISTORY' status.
      :return: List of business statuses.
      """
      dict_list = []
      status_list = ['ACTIVE', 'CLOSED', 'HISTORY']
      weight_list = [weightAct, weightCls, weightHis]
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_weighted_string_list(status_list, weight_list))
      return dict_list

# Generate the Business Company Name field
def generate_random_company_name_field(num_records):
      """
      Generate a list of random company names for a specified number of records.
      :param num_records: Number of company names to generate.
      :return: List of company names.
      """
      dict_list = []
      for _ in range(num_records):
            adjective = random.choice(bus_list_adjectives)
            noun = random.choice(bus_list_nouns)
            keyword = random.choice(bus_list_keywords)
            dict_list.append(f"{adjective} {keyword} {noun}")
      return dict_list

# Generate the Business Account Type field
def generate_random_account_type_field(num_records, num_acct_types = 10):
      """
      Generate a list of random account types for a specified number of records.
      :param num_records: Number of account types to generate.
      :param num_acct_types: Number of unique account types to choose from.
      :return: List of account types.
      """
      dict_list = []
      acct_type_list = []
      for _ in range(num_acct_types):
            acct_type_list.append(gtsf.generate_random_letter(4))
      for _ in range(num_records):
            dict_list.append(random.choice(acct_type_list))
      return dict_list

# Generate the Business Creation Date field
def generate_random_creation_date_field(num_records, min_date = datetime(1990,1,1), max_date = datetime.now()):
      """
      Generate a list of random creation dates within a specified date range.
      :param num_records: Number of dates to generate.
      :param min_date: Minimum date in the range.
      :param max_date: Maximum date in the range.
      :return: List of creation dates.
      """
      min_date = gtsf.function_date_int_to_datetime(min_date)
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_date(min_date, max_date))
      return dict_list

# Generate the Business Modified Date field
def generate_random_modified_date_field(num_records, created_date_list, max_date = datetime.now()):
      """
      Generate a list of random modified dates based on creation dates and a maximum date.
      :param num_records: Number of dates to generate.
      :param created_date_list: List of creation dates.
      :param max_date: Maximum date for modification.
      :return: List of modified dates.
      """
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            dict_list.append(gtsf.generate_date(created_date_list[x], max_date))
      return dict_list

# Generate the Business Closed Date field
def generate_random_closed_date_field(num_records, status_list, mod_date_list, max_date = datetime.now()):
      """
      Generate a list of random closed dates for businesses, based on their status and modification dates.
      :param num_records: Number of dates to generate.
      :param status_list: List of business statuses.
      :param mod_date_list: List of modification dates.
      :param max_date: Maximum date for closing.
      :return: List of closed dates.
      """
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            if status_list[x] == 'CLOSED' or status_list[x] == 'HISTORY':
                  dict_list.append(gtsf.generate_date(mod_date_list[x], max_date))
            else:
                  dict_list.append(None)
      return dict_list

# Generate the Business TAG field
def generate_random_tag_field(num_records, num_tag = 10):
      """
      Generate a list of random business tags for a specified number of records.
      :param num_records: Number of tags to generate.
      :param num_tag: Number of unique tags to choose from.
      :return: List of business tags.
      """
      dict_list = []
      tag_list = []
      for _ in range(num_tag):
            tag_list.append(gtsf.generate_random_letter(3))
      for _ in range(num_records):
            dict_list.append(random.choice(tag_list))
      return dict_list

# Generate the Business Security Category field
def generate_random_system_cat_field(num_records, min_cat = 0, max_cat = 5):
      """
      Generate a list of random security categories within a specified range for a number of records.
      :param num_records: Number of categories to generate.
      :param min_cat: Minimum category value.
      :param max_cat: Maximum category value.
      :return: List of security categories.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.randint(min_cat, max_cat))
      return dict_list



#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 
#----------              Generate the Business Table                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Function to run each field to build the business table
def generate_table_business_general(dict, id_field_name = 'ID_Record'):  
      """
      Populate a dictionary with various business-related data fields to build a business table.
      :param dict: Dictionary to populate with business data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with business data fields.
      """
      num_records = len(dict[id_field_name])
      dict_list_id = dict[id_field_name]
      dict['Account'] = generate_account_field(dict_list_id, num_records)
      dict['Branch'] = generate_random_branch_field(num_records)
      dict['External ID'] = [branch + account for branch, account in zip(dict['Branch'], dict['Account'])]
      dict['Business Status'] = generate_random_status_field(num_records)
      dict['Company Name'] = generate_random_company_name_field(num_records)
      dict['Account Type'] = generate_random_account_type_field(num_records,9)
      # - - - Date Format: YYYYMMDD - - -
      dict['Creation Date'] = generate_random_creation_date_field(num_records)
      dict['Modified Date'] = generate_random_modified_date_field(num_records, dict['Creation Date'])
      dict['Closed Date'] = generate_random_closed_date_field(num_records, dict['Business Status'], dict['Modified Date'])
      # - - - - - - - - - - - - - - - - -
      dict['Business TAG'] = generate_random_tag_field(num_records,3)
      dict['Security Category'] = generate_random_system_cat_field(num_records)
      return dict

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

# def generate_table_business(min_rand_record_lim = 1, max_rand_record_lim = 100000):
#       """
#       Generate a table of business data with random data.
#       :param min_rand_record_lim: Minimum limit for random record length.
#       :param max_rand_record_lim: Maximum limit for random record length.
#       :return: Dictionary representing the generated business table.
#       """
#       bus_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
#       bus_data = gtsf.table_generate_id_records(bus_num_records)
#       bus_data = generate_table_business_build(bus_data, bus_num_records)
#       return bus_data

