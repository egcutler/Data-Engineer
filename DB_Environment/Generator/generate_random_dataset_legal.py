import pandas as pd
import random
import string
from datetime import datetime, timedelta
import generate_random_dataset_support_functions as gtsf

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Legal List for Support Functions                 ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Legal surname list for random generator
legal_list_surnames = [
    "Anderson", "Baker", "Carter", "Davis", "Evans", "Fisher", "Garcia", 
    "Harris", "Jackson", "King", "Lewis", "Martin", "Nelson", "Owens", 
    "Parker", "Quinn", "Roberts", "Smith", "Taylor", "Underwood", "Vasquez", 
    "Williams", "Young", "Zimmerman"
]

# Legal term list for random generator
legal_list_terms = [
    "Legal", "Law", "Justice", "Advocates", "Solicitors", "Counsel", 
    "Barristers", "Attorneys", "Partners", "Associates", "Consultants", 
    "Advisors", "Counselors", "Litigators", "Defenders", "Prosecutors"
]

# Legal type dictionary for random generator
dict_leg_type = {
      'BANK' : 'Bank Division',
      'CREDIT' : 'Credit Account',
      'TRADR' : 'Trader credential account',
      'AFFRS' : 'Affairs',
      'AFF' : 'Available Funds File',
      'CORP' : 'Corporation Division',
      'AG' : 'Agriculture',
      'ADVIS' : 'Legal Advisor',
      'BENE' : 'Beneficiary credentail for investment',
      'AGENT' : 'An agent bank acts as a bank performing some \
specific duties on behalf of another party',
      'GUNTE' : 'The bank guarantee means that the lender will \
ensure that the liabilities of a debtor will be met. In other \
words, if the debtor fails to settle a debt, the bank will cover it',
      'TTEE' : 'In the case of the certificate of deposit, the \
trustee is most likely someone charged with taking care of the \
money until the person it is intended for comes of an age to receive it',
      'AFD' : 'Allowance For Depreciation'
}

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Legal Functions for Generator                   ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Generate the Legal ID field
def generate_legal_account_field(num_records, len_id_char = 8):
      """
      Generate a list of legal account IDs with a specified character length.
      :param num_records: Number of account IDs to generate.
      :param len_id_char: Length of each ID in characters (default is 8).
      :return: List of legal account IDs.
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

# Generate the Legal firm field
def generate_legal_firm_field(num_records):
      """
      Generate a list of legal firm names.
      :param num_records: Number of firm names to generate.
      :return: List of legal firm names.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_legal_firm_name(legal_list_surnames, legal_list_terms))
      return dict_list

# Generate the Legal type and definition fields
def generate_legal_type_and_def_field(num_records):
      """
      Generate lists of legal types and their definitions.
      :param num_records: Number of records to generate.
      :return: Two lists, one for legal types and one for their definitions.
      """
      dict_list_type = []
      dict_list_def = []
      for _ in range(num_records):
            le_type, le_type_def = gtsf.generate_legal_type_and_def(dict_leg_type)
            dict_list_type.append(le_type)
            dict_list_def.append(le_type_def)
      return dict_list_type, dict_list_def

# Generate the Legal Status field
def generate_legal_status_field(num_records, weightAct = 60, weightCls = 10, weightHis = 10):
      """
      Generate a list of legal statuses with specified weighting.
      :param num_records: Number of statuses to generate.
      :param weightAct: Weight for 'ACTIVE' status.
      :param weightCls: Weight for 'CLOSED' status.
      :param weightHis: Weight for 'HISTORY' status.
      :return: List of legal statuses.
      """
      dict_list = []
      status_list = ['ACTIVE', 'CLOSED', 'HISTORY']
      weight_list = [weightAct, weightCls, weightHis]
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_weighted_string_list(status_list, weight_list))
      return dict_list

# Generate the Legal Creation Date field
def generate_legal_creation_date_field(num_records, min_date = datetime(1990,1,1), max_date = datetime.now()):
      """
      Generate a list of legal creation dates within a specified date range.
      :param num_records: Number of dates to generate.
      :param min_date: Minimum date for the range.
      :param max_date: Maximum date for the range.
      :return: List of legal creation dates.
      """
      min_date = gtsf.function_date_int_to_datetime(min_date)
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_date(min_date, max_date))
      return dict_list

# Generate the Legal Modified Date field
def generate_legal_modified_date_field(num_records, created_date_list, max_date = datetime.now()):
      """
      Generate a list of legal modified dates based on creation dates and a maximum date.
      :param num_records: Number of dates to generate.
      :param created_date_list: List of creation dates.
      :param max_date: Maximum date for modification.
      :return: List of legal modified dates.
      """
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            dict_list.append(gtsf.generate_date(created_date_list[x], max_date))
      return dict_list

# Generate the Legal Closed Date field
def generate_legal_closed_date_field(num_records, status_list, mod_date_list, max_date = datetime.now()):
      """
      Generate a list of legal closed dates for firms, based on their status and modification dates.
      :param num_records: Number of dates to generate.
      :param status_list: List of legal statuses.
      :param mod_date_list: List of modification dates.
      :param max_date: Maximum date for closing.
      :return: List of legal closed dates.
      """
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            if status_list[x] == 'CLOSED' or status_list[x] == 'HISTORY':
                  dict_list.append(gtsf.generate_date(mod_date_list[x], max_date))
            else:
                  dict_list.append(None)
      return dict_list

# Generate the Legal Tax Category Field
def generate_legal_tax_cat_field(num_records):
      """
      Generate a list of legal tax categories.
      :param num_records: Number of tax categories to generate.
      :return: List of legal tax categories.
      """
      dict_list=[]
      le_tax_cat_list = ['G','M','N','I','D','Ba', 'Bt']
      for _ in range(num_records):
            dict_list.append(random.choice(le_tax_cat_list))
      return dict_list

# Generate the Legal IRS TIN ID field
def generate_legal_irs_tin_id_field(num_records, len_id_char = 7):
      """
      Generate a list of IRS TIN IDs for legal entities.
      :param num_records: Number of IRS TIN IDs to generate.
      :param len_id_char: Length of each ID in characters (default is 7).
      :return: List of IRS TIN IDs.
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
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

# Generate the Legal MPID field
def generate_legal_mpid_field(num_records, len_id_char = 7):
      """
      Generate a list of MPID (Market Participant Identifier) for legal entities.
      :param num_records: Number of MPID to generate.
      :param len_id_char: Length of each ID in characters (default is 7).
      :return: List of MPID.
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
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

# Generate the Legal GIIN ID field
def generate_legal_giin_id_field(num_records, len_id_char = 7):
      """
      Generate a list of GIIN (Global Intermediary Identification Number) for legal entities.
      :param num_records: Number of GIIN IDs to generate.
      :param len_id_char: Length of each ID in characters (default is 7).
      :return: List of GIIN IDs.
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
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

# Generate the Legal FACTA ID field
def generate_legal_facta_id_field(num_records, len_id_char = 7):
      """
      Generate a list of FACTA IDs for legal entities.
      :param num_records: Number of FACTA IDs to generate.
      :param len_id_char: Length of each ID in characters (default is 7).
      :return: List of FACTA IDs.
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
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

# Generate the Legal WCIS field
def generate_legal_wcis_id_field(num_records, len_id_char = 7):
      """
      Generate a list of WCIS (Worldwide Common Identifier System) for legal entities.
      :param num_records: Number of WCIS IDs to generate.
      :param len_id_char: Length of each ID in characters (default is 7).
      :return: List of WCIS IDs.
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
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

# Generate the Legal TEFRA ID field
def generate_legal_tefra_id_field(num_records, len_id_char = 7):
      """
      Generate a list of TEFRA (Tax Equity and Fiscal Responsibility Act) IDs for legal entities.
      :param num_records: Number of TEFRA IDs to generate.
      :param len_id_char: Length of each ID in characters (default is 7).
      :return: List of TEFRA IDs.
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
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Legal Table                       ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Function to run each field to build the legal table
def generate_table_legal_general(dict, id_field_name = 'ID_Record'): 
      """
      Populate a dictionary with various legal-related data fields to build a legal table.
      :param dict: Dictionary to populate with legal data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with legal data fields.
      """
      num_records = len(dict[id_field_name])
      dict['Legal Account'] = generate_legal_account_field(num_records, 8)
      dict['Legal Firm'] = generate_legal_firm_field(num_records)
      dict['Legal Type'], dict['Legal Type Def'] = generate_legal_type_and_def_field(num_records)
      dict['Legal Status'] = generate_legal_status_field(num_records)
      # - - - Date Format: YYYYMMDD - - -
      dict['LE Creation Date'] = generate_legal_creation_date_field(num_records)
      dict['LE Modified Date'] = generate_legal_modified_date_field(num_records, dict['LE Creation Date'])
      dict['LE Closed Date'] = generate_legal_closed_date_field(num_records, dict['Legal Status'], dict['LE Modified Date'])
      # - - - - - - - - - - - - - - - - -
      dict['Legal Tax Category'] = generate_legal_tax_cat_field(num_records)
      dict['IRS TIN ID'] = generate_legal_irs_tin_id_field(num_records)
      dict['MPID'] = generate_legal_mpid_field(num_records, 6)
      dict['GIIN ID'] = generate_legal_giin_id_field(num_records, 6)
      dict['FACTA ID'] = generate_legal_facta_id_field(num_records, 9)
      dict['WCIS ID'] = generate_legal_wcis_id_field(num_records, 5)
      dict['TEFRA ID'] = generate_legal_tefra_id_field(num_records)
      return dict

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

# # Main function to run the legal table generator  
# def generate_table_legal(min_rand_record_lim = 1, max_rand_record_lim = 100000):
#       """
#       Generate a table of legal data with random data.
#       :param min_rand_record_lim: Minimum limit for random record length.
#       :param max_rand_record_lim: Maximum limit for random record length.
#       :return: Dictionary representing the generated legal table.
#       """
#       le_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
#       le_data = gtsf.table_generate_id_records(le_num_records)
#       le_data = generate_table_legal_build(le_data, le_num_records)
#       return le_data