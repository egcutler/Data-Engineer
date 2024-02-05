import pandas as pd
import random
from datetime import datetime, timedelta
import generate_random_dataset_support_functions as gtsf

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Employee List for Support Functions              ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Employee first name list for random generator
first_names = ["John", "Jane", "Alex", "Emily", "David", "Sarah", "Michael", "Olivia", 
               "Daniel", "Emma", "Chris", "Anna", "James", "Sophia", "Robert", "Isabella", 
               "William", "Mia", "Joseph", "Amelia", "Richard", "Evelyn", "Charles", 
               "Abigail", "Thomas", "Harper", "Mary", "Ethan", "Jessica", "Benjamin"]

# Employee last name list for random generator
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", 
              "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", 
              "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White",
              "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Robinson", 
              "Walker", "Perez", "Hall"]

# Employee job dictionary for random generator
dict_jobs = {
      'Business Analyst' : ['Operations Manager', 'Project Manager'],
      'Data Engineer' : ['Operations Manager', 'Project Manager', 'Engineer Manager'],
      'Data Analyst' : ['Operations Manager', 'Project Manager'],
      'Dev Ops Engineer' : ['Operations Manager', 'Project Manager'],
      'Financial Analyst' : ['Operations Manager', 'Project Manager', 'Product Manager', 'Finance manager'],
      'IT Specialist' : ['IT Manager'],
      'Engineer Specialist' : ['Engineer Manager'],
      'Sales and Stragety' : ['Sales Manager'],
      'Supply Chain Coordinator' : ['Project Manager', 'Product Manager'],
      'Quality Assurance Tester' : ['Project Manager', 'Product Manager'],
      'Web Developer' : ['Operations Manager', 'Project Manager', 'Product Manager', 'Marketing Manager'],
      'Social Media Specialist' : ['Marketing Manager'],
      'Customer Service Representative' : ['Customer Success Manager'],
      'Human Resources' : ['Human Resources Manager'],
      'Administrative Assistant' : ['IT Manager'],
      'Legal Assistant' : ['Legal Manager'],
      'Software Engineer' : ['Operations Manager', 'Project Manager', 'Product Manager', 'Engineer Manager'],
      'Graphic Designer' : ['Operations Manager', 'Project Manager', 'Product Manager', 'Engineer Manager'],
      'Sales Representative' : ['Sales Manager'],
      'Research Scientist' : ['Operations Manager', 'Project Manager', 'Product Manager', 'Marketing Manager', 'Engineer Manager'],
      'Accountant' : ['Finance manager']  
}

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Employee Functions for Generator                ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Generate the Employee ID field
def generate_emp_id_field(num_records, len_id_char = 7):
      """
      Generate a list of unique employee IDs with a specified character length.
      :param num_records: Number of IDs to generate.
      :param len_id_char: Length of each ID in characters (default is 7).
      :return: List of employee IDs.
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

# Generate the Employee First Name field
def generate_emp_first_name_field(num_records):
      """
      Generate a list of random employee first names from a predefined list.
      :param num_records: Number of first names to generate.
      :return: List of employee first names.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.choice(first_names))
      return dict_list

# Generate the Employee First Name field
def generate_emp_last_name_field(num_records):
      """
      Generate a list of random employee last names from a predefined list.
      :param num_records: Number of last names to generate.
      :return: List of employee last names.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(random.choice(last_names))
      return dict_list

# Generate the Employee Phone Number field
def generate_emp_phone_number_field(num_records):
      """
      Generate a list of random employee phone numbers.
      :param num_records: Number of phone numbers to generate.
      :return: List of employee phone numbers.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_phone_number())
      return dict_list

# Generate the Employee Job Title field
def generate_emp_job_title_field(num_records):
      """
      Generate a list of random employee job titles from a predefined dictionary.
      :param num_records: Number of job titles to generate.
      :return: List of employee job titles.
      """
      dict_list = []
      job_titles = list(dict_jobs.keys())
      for _ in range(num_records):
            dict_list.append(random.choice(job_titles))
      return dict_list

# Generate the Employee Email field
def generate_emp_email_field(num_records, first_name, last_name):
      """
      Generate a list of employee email addresses based on their first and last names.
      :param num_records: Number of email addresses to generate.
      :param first_name: List of employee first names.
      :param last_name: List of employee last names.
      :return: List of employee email addresses.
      """
      dict_list = []
      for x in range(num_records):
            dict_list.append(f'{last_name[x]}.{first_name[x]}@fakemail.com')
      return dict_list

# Generate the Employee Status field
def generate_emp_status_field(num_records, weightY = 90, weightN = 10):
      """
      Generate a list of random employee statuses with specified weighting.
      :param num_records: Number of statuses to generate.
      :param weightY: Weight for 'EMPLOYEED' status.
      :param weightN: Weight for 'TERMINATED' status.
      :return: List of employee statuses.
      """
      dict_list = []
      status_list = ['EMPLOYEED', 'TERMINATED']
      weight_list = [weightY, weightN]
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_weighted_string_list(status_list, weight_list))
      return dict_list

# Generate the Employee Hire Date field
def generate_emp_hire_date_field(num_records, min_date = datetime(1990,1,1), max_date = datetime.now()):
      """
      Generate a list of random employee hire dates within a specified date range.
      :param num_records: Number of dates to generate.
      :param min_date: Minimum date in the range.
      :param max_date: Maximum date in the range.
      :return: List of hire dates.
      """
      min_date = gtsf.function_date_int_to_datetime(min_date)
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_date(min_date, max_date))
      return dict_list

# Generate the Employee Termination field
def generate_emp_termination_field(num_records, status_list, hire_date_list, max_date = datetime.now()):
      """
      Generate a list of random employee termination dates based on their status and hire dates.
      :param num_records: Number of termination dates to generate.
      :param status_list: List of employee statuses.
      :param hire_date_list: List of employee hire dates.
      :param max_date: Maximum date for termination.
      :return: List of termination dates.
      """
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for x in range(0, num_records):
            if status_list[x] == 'TERMINATED':
                  dict_list.append(gtsf.generate_date(hire_date_list[x], max_date))
            else:
                  dict_list.append(None)
      return dict_list

# Generate the Employee Manager First name Field
def generate_emp_manager_fields(num_records, emp_first_name, emp_last_name, emp_job_title_list):
      """
      Generate lists of manager names and positions for employees based on their job titles.
      :param num_records: Number of records to generate.
      :param emp_first_name: List of employee first names.
      :param emp_last_name: List of employee last names.
      :param emp_job_title_list: List of employee job titles.
      :return: Lists of manager first names, last names, and positions.
      """
      dict_list_firstname = []
      dict_list_lastname = []
      dict_list_manager = []
      
      for x in range(num_records):
            mang_first_name = random.choice(first_names)
            while mang_first_name == emp_first_name[x]:
                  mang_first_name = random.choice(first_names)        
            dict_list_firstname.append(mang_first_name)
            
            mang_last_name = random.choice(last_names)
            while mang_last_name == emp_last_name[x]:
                  mang_last_name = random.choice(last_names)        
            dict_list_lastname.append(mang_last_name)
            
            dict_list_manager.append(random.choice(dict_jobs[emp_job_title_list[x]]))
            
      return dict_list_firstname, dict_list_lastname, dict_list_manager

# Generate the Employee Manager Security Clearance field
def generate_emp_security_clearance_field(num_records, min = 1, max = 5):
      """
      Generate a list of random employee security clearance levels within a specified range.
      :param num_records: Number of clearance levels to generate.
      :param min: Minimum clearance level.
      :param max: Maximum clearance level.
      :return: List of security clearance levels.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_int(min, max))
      return dict_list

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Employee Table                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Function to run each field to build the employee table
def generate_table_employee_general(dict, id_field_name = 'ID_Record'): 
      """
      Populate a dictionary with various employee-related data fields to build an employee table.
      :param dict: Dictionary to populate with employee data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with employee data fields.
      """
      num_records = len(dict[id_field_name])
      dict['Employee ID'] = generate_emp_id_field(num_records)
      dict['Emp First Name'] = generate_emp_first_name_field(num_records)
      dict['Emp Last Name'] = generate_emp_last_name_field(num_records)
      dict['Emp Phone Number'] = generate_emp_phone_number_field(num_records)
      dict['Job Title'] = generate_emp_job_title_field(num_records)
      dict['Employee Email'] = generate_emp_email_field(num_records, dict['Emp First Name'], dict['Emp Last Name'])
      dict['Employee Status'] = generate_emp_status_field(num_records)
      # - - - Date Format: YYYYMMDD - - -
      dict['Hire Date'] = generate_emp_hire_date_field(num_records)
      # - - - - - - - - - - - - - - - - -
      dict['Termination Date'] = generate_emp_termination_field(num_records, dict['Employee Status'], dict['Hire Date'])
      dict['Manager First Name'], dict['Manager Last Name'], dict['Manager Position'] = generate_emp_manager_fields(num_records, dict['Emp First Name'], dict['Emp Last Name'], dict['Job Title'])
      dict['Security Clearance'] = generate_emp_security_clearance_field(num_records)
      return dict

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

# # Main function to run the employee table generator
# def generate_table_employee(min_rand_record_lim = 1, max_rand_record_lim = 100000):
#       """
#       Generate a table of employee data with random data.
#       :param min_rand_record_lim: Minimum limit for random record length.
#       :param max_rand_record_lim: Maximum limit for random record length.
#       :return: Dictionary representing the generated employee table.
#       """
#       emp_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
#       emp_data = gtsf.table_generate_id_records(emp_num_records)
#       emp_data = generate_table_employee_build(emp_data, emp_num_records)
#       return emp_data

