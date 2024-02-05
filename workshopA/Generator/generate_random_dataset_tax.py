import pandas as pd
import random
from datetime import datetime, timedelta
import generate_random_dataset_support_functions as gtsf

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Tax List for Support Functions                   ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Tax type dictionary for random generator
dict_tax_types = {
      'ADJ' : 'Adjustment',
      'BEN/BENF' : 'Benefit(s)',
      'LTI' : 'Loan to Income',
      'IHT' : 'Inheritance Tax',
      'CAR' : 'Centralized Accounts Receivable',
      'FoF' : 'Fund of Funds',
      'CWP' : 'Conventional With Profits',
      'ADMIS' : 'Admission',
      'C+MV' : 'Cost Plus Market Value',
      'Q1' : 'First quarter of the year',
      'A/R' : 'Accounts Receivable',
      'WPA' : 'With Profits Actuary / With Profits Annuity',
      'NBV' : 'Net Book Value',
      'APC/APD' : 'Amended Payroll Certification/Distribution',
      'B & C' : 'Bonds And Coupons',
      'WPICC' : 'With Profits Insurance Capital Component',
      'VaR' : 'Value at Risk',
      'EC' : 'European Commission',
      'TV' : 'Transfer Value',
      'Q4' : 'Fourth quarter of the year',
      'ADDL' : 'Additional',
      'CTF' : 'Child Trust Fund',
      'CESR' : 'Committee of European Securities Regulators',
      'CIMPS' : 'Contracted-in Money Purchase Scheme',
      'CDS' : 'Credit Default Swap',
      'C/S' : 'Cost Sharing',
      'AFFRS' : 'Affairs',
      'AFD' : 'Allowance For Depreciation',
      'DGI' : 'Domestically Generated Inflation',
      'ABS' : 'Absences - As In Compensated Absences',
      'OMO' : 'Open Market Option',
      'PBT' : 'Profit before Taxes',
      'MBO' : 'Management Buy Out',
      'RCM' : 'Risk Capital Margin',
      'CAP.' : 'Capital',
      'ETF' : 'Exchange Traded Funds',
      'MBI' : 'Management Buy In',
      'BA' : 'Bank Adjustments',
      'ADT' : 'Auditing',
      'EBT' : 'Earnings Before Taxes',
      'PV' : 'Present Value',
      'RoC' : 'Return on Capital',
      'Q3' : 'Third quarter of the year',
      'PAT' : 'Profit after Taxes',
      'APPROP' : 'Appropriations',
      'COMPS' : 'Contracted-out Money Purchase Scheme',
      'ABACCR' : 'Absences Accrual - (As In Compensated Absences Accrual)',
      'CT' : 'Corporation Tax',
      'FoHF' : 'Fund of Hedge Funds',
      'UHNW' : 'Ultra High Net Worth',
      'FTT' : 'Financial Transaction Tax',
      'WoM' : 'Whole of Market',
      'NAV' : 'Net Asset Value',
      'Q2' : 'Second quarter of the year',
      'AID' : 'Agency For International Development',
      'ADMIN' : 'Administrative'
}

# Tax entry cd list for random generator
list_entrycd = [
      'DIV', 'INT'
]

# Tax currency list for random generator
list_cur = [
      'USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD'
]

# Tax debit and credit list for random generator
list_debit_and_credit = ['Debit','Credit']

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Tax Functions for Generator                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
# Generate the Tax Account field
def generate_tax_account_field(num_records, len_id_char = 8):
      """
      Generate a list of tax account numbers with a specified character length.
      :param num_records: Number of account numbers to generate.
      :param len_id_char: Length of each account number in characters (default is 8).
      :return: List of tax account numbers.
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

# Generate the Tax Security ID field
def generate_tax_sec_id_field(num_records, min = 100000, max = 9999999):
      """
      Generate a list of security IDs for tax purposes.
      :param num_records: Number of security IDs to generate.
      :param min: Minimum value for security ID.
      :param max: Maximum value for security ID.
      :return: List of security IDs.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

# Generate the Tax CUSIP field
def generate_tax_cusip_field(num_records, len_id_char = 7):
      """
      Generate a list of CUSIP (Committee on Uniform Securities Identification Procedures) numbers.
      :param num_records: Number of CUSIP numbers to generate.
      :param len_id_char: Length of each CUSIP number in characters (default is 7).
      :return: List of CUSIP numbers.
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

# Generate the Tax Entry CD field
def generate_tax_entrycd_field(num_records):
      """
      Generate a list of entry codes for tax transactions.
      :param num_records: Number of entry codes to generate.
      :return: List of entry codes.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.choice(list_entrycd))
      return dict_list

# Generate the Tax Currency field
def generate_tax_currency_field(num_records, priority_item = 'USD', weight_usd = 10, weight_oth = 1):
      """
      Generate a list of currencies with weighted preference for a specific currency.
      :param num_records: Number of currencies to generate.
      :param priority_item: Currency to prioritize (default 'USD').
      :param weight_usd: Weight for the prioritized currency (default 10).
      :param weight_oth: Weight for other currencies (default 1).
      :return: List of currencies.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_unique_weighted_list(list_cur, priority_item, weight_usd, weight_oth))
      return dict_list

# Generate the Tax Net Amount field
def generate_tax_net_amount_field(num_records, min = 1, max = 99999):
      """
      Generate a list of net amounts for tax transactions.
      :param num_records: Number of net amounts to generate.
      :param min: Minimum value for net amount.
      :param max: Maximum value for net amount.
      :return: List of net amounts.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

# Generate the Tax Withholding Amount field
def generate_tax_withholding_amount_field(num_records, min = 1, max = 9999):
      """
      Generate a list of withholding amounts for tax transactions.
      :param num_records: Number of withholding amounts to generate.
      :param min: Minimum value for withholding amount.
      :param max: Maximum value for withholding amount.
      :return: List of withholding amounts.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

# Generate the Tax Debit and Credit field
def generate_tax_debit_and_credit_field(num_records):
      """
      Generate a list of debit and credit statuses for tax transactions.
      :param num_records: Number of statuses to generate.
      :return: List of debit and credit statuses.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.choice(list_debit_and_credit))
      return dict_list

# Generate the Tax Type field
def generate_tax_type_field(num_records):
      """
      Generate a list of tax types.
      :param num_records: Number of tax types to generate.
      :return: List of tax types.
      """
      dict_list = []
      tax_types = list(dict_tax_types.keys())
      for _ in range(num_records):
            dict_list.append(random.choice(tax_types))
      return dict_list

# Generate the Tax Type Description field
def generate_tax_type_desc_field(num_records, tax_type_list):
      """
      Generate descriptions for the given tax types.
      :param num_records: Number of descriptions to generate.
      :param tax_type_list: List of tax types.
      :return: List of tax type descriptions.
      """
      dict_list = []
      for x in range(num_records):
            dict_list.append(dict_tax_types[tax_type_list[x]])
      return dict_list

# Generate the Tax Transaction Date field
def generate_tax_trans_date_field(num_records, min_date = datetime(2010,1,1), max_date = datetime.now()):
      """
      Generate a list of transaction dates for tax purposes within a specified range.
      :param num_records: Number of transaction dates to generate.
      :param min_date: Minimum date for the range.
      :param max_date: Maximum date for the range.
      :return: List of transaction dates.
      """
      min_date = gtsf.function_date_int_to_datetime(min_date)
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_date(min_date, max_date))
      return dict_list

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Tax Table                          ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Function to run each field to build the tax table
def generate_table_tax_general(dict, id_field_name = 'ID_Record'):  
      """
      Populate a dictionary with various tax-related data fields to build a tax table.
      :param dict: Dictionary to populate with tax data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with tax data fields.
      """
      num_records = len(dict[id_field_name])
      dict['Tax Account'] = generate_tax_account_field(num_records)
      dict['Sec ID'] = generate_tax_sec_id_field(num_records)
      dict['CUSIP'] = generate_tax_cusip_field(num_records)
      dict['Entry CD'] = generate_tax_entrycd_field(num_records)
      dict['Currency'] = generate_tax_currency_field(num_records)
      dict['Net Amount'] = generate_tax_net_amount_field(num_records)
      dict['Withholding Amount'] = generate_tax_withholding_amount_field(num_records)
      dict['Credit and Debit'] = generate_tax_debit_and_credit_field(num_records)
      dict['Tax Type'] = generate_tax_type_field(num_records)
      dict['Tax Type Definition'] = generate_tax_type_desc_field(num_records, dict['Tax Type'])
      # - - - Date Format: YYYYMMDD - - -
      dict['Transaction Date'] = generate_tax_trans_date_field(num_records)
      # - - - - - - - - - - - - - - - - -
      return dict

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

# # Main function to run the tax table generator
# def generate_table_tax(min_rand_record_lim = 1, max_rand_record_lim = 100000):
#       """
#       Generate a table of tax data with random data.
#       :param min_rand_record_lim: Minimum limit for random record length.
#       :param max_rand_record_lim: Maximum limit for random record length.
#       :return: Dictionary representing the generated tax table.
#       """
#       tax_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
#       tax_data = gtsf.table_generate_id_records(tax_num_records)
#       tax_data = generate_table_tax_build(tax_data, tax_num_records)
#       return tax_data