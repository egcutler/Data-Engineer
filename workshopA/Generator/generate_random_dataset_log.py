import random
from datetime import datetime
import generate_random_dataset_support_functions as gtsf

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Log List for Support Functions                   ---------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Log Event Type dictionary for random generator
log_dict_event = {
      "User Activity" : "Logged the user activity",
      "Server Event" : "Logged the server activity",
      "Data Change" : "Logged a change in data",
      "File Change" : "Logged a change in a file",
      "System Error" : "Logged a system error",
      "Security Alert" : "Logged a potential security breach"
}

# Log Description dictionaries for random generator
log_dict_data_change = {
      "Create": "Adding new data or records to the system. This could involve creating a new user account, adding a new product to a catalog, or entering new transaction details.",
      "Update": "Modifying existing data or records. This includes changes like updating user information, altering product prices, or revising transaction amounts.",
      "Delete": "Removing data or records from the system. This might involve deleting a user account, removing a product from the catalog, or voiding a transaction.",
      "Archive": "Moving data to an archival state rather than deleting it. This allows for the preservation of data for historical or compliance purposes while reducing its active footprint in the system.",
      "Merge": "Combining multiple data records into a single record. This is often used in scenarios like deduplicating customer records or consolidating transaction details.",
      "Split": "Separating a single data record into multiple records. This might be used in cases where a single transaction needs to be divided into multiple parts for accounting purposes.",
      "Rollback": "Reverting data to a previous state or version. This is used in scenarios where recent changes need to be undone.",
      "Import": "Bringing in data from external sources. This could involve bulk uploading of data, such as importing a list of contacts or product details.",
      "Export": "Sending data out to external systems or files. This typically involves generating reports or datasets for analysis or sharing with external parties.",
      "Data Cleansing": "Correcting or removing inaccurate records from a dataset. This ensures the quality and reliability of the data in the system."
}

log_dict_file_change = {
      "File Upload": "Notes when a user uploads a file, including details like file type and size.",
      "File Deletion": "Logs the removal of a file from the system, detailing the file name and deletion time.",
      "File Rename": "Records the action of changing a file's name, noting the original and new names of the file.",
      "Form Submission": "Logs when a user submits a form, such as a contact form, registration form, or a settings change form.",
      "File Modification": "Tracks changes made to a file, including edits to the content, format changes, or metadata updates.",
      "File Download": "Records when a user downloads a file, including the file name and time of download.",
      "File Access": "Logs each instance of a file being accessed or opened by a user, noting the file name and access time.",
      "File Move": "Tracks when a file is moved from one location to another, recording the original and new locations.",
      "File Copy": "Notes when a user makes a copy of a file, including details of the source and destination locations.",
      "File Permission Change": "Logs changes made to file permissions, detailing the file name and the updated permissions."
}

log_dict_security = {
      "Unauthorized Access Attempt": "Logs attempts to access the system or data without proper authorization.",
      "Password Change Attempt": "Records attempts to change a password, whether successful or not.",
      "Firewall Alert": "Logs alerts triggered by the firewall, indicating potential security threats.",
      "Virus Detection": "Records instances where a virus or malware is detected by the system's antivirus software.",
      "Data Breach": "Logs incidents where sensitive data is accessed or exposed in an unauthorized manner.",
      "Security Patch Application": "Tracks the application of security patches to the system or software.",
      "Encryption Status Change": "Logs changes in the encryption status of data, such as enabling or disabling encryption.",
      "User Role Change": "Records changes in user roles, especially changes that affect access privileges.",
      "Security Policy Update": "Logs updates or changes to security policies within the system.",
      "Two-factor Authentication Event": "Tracks events related to two-factor authentication, including setup, changes, and authentication attempts.",
      "Security Scan": "Records the outcomes of security scans, detailing identified vulnerabilities or anomalies.",
      "Suspicious Activity": "Logs activities flagged as suspicious, which could indicate a potential security threat."
}

log_dict_user_web = {
      "Login Attempt": "Tracks each attempt a user makes to log in, whether successful or not.",
      "Logout Attempt": "Tracks each attempt a user makes to log out, whether successful or not.",
      "Comment Posting": "Tracks user comments on posts, articles, or other users' content.",
      "Page Visit": "Records when a user visits a specific page or section of the application or website.",
      "Search Query": "Logs the search terms a user enters in a search bar within the application.",
      "Video View": "Tracks when a user views a video, including information on the video watched and duration of view.",
      "Notification Interaction": "Records interactions with notifications, such as opening or dismissing them.",
      "Profile Update": "Logs changes made to a user's profile, including photo updates, bio changes, etc.",
      "File Upload": "Notes when a user uploads a file, including details like file type and size.",
      "Item Purchase": "Records when a user makes a purchase, detailing the items bought and the transaction details.",
      "Form Submission": "Logs when a user submits a form, such as a contact form, registration form, or a settings change form.",
      "Social Media Share": "Logs when a user shares content from the application on social media platforms."
}


log_dict_user_server = {
      "Server Start": "Logs when the server is started, including the timestamp and initial status.",
      "Server Shutdown": "Records when the server is shut down, noting the time and reason for shutdown.",
      "Service Start": "Tracks the initiation of a specific service on the server, including service name and start time.",
      "Service Stop": "Logs when a service on the server is stopped, detailing the service name and stop time.",
      "System Update": "Records updates made to the server's operating system or software packages.",
      "Security Alert": "Logs security-related events, such as unauthorized access attempts or detected vulnerabilities.",
      "Performance Metrics": "Tracks various performance metrics of the server, like CPU usage, memory usage, and disk space.",
      "Backup Completion": "Records the completion of data backup processes, including time and status of the backup.",
      "Error Reports": "Logs error events, with details about the error type, affected components, and timestamps.",
      "Configuration Change": "Tracks changes made to server configurations, such as network settings or system parameters.",
      "Network Activity": "Logs network-related activities, including incoming and outgoing traffic details.",
      "Hardware Status": "Records the status of server hardware components, such as hard drives, memory modules, and CPUs."
}

log_dict_user_accout = {
      "Login Attempt": "Tracks each attempt a user makes to log in, whether successful or not.",
      "Logout Attempt": "Tracks each attempt a user makes to log out, whether successful or not.",
      "Settings Change": "Tracks changes a user makes to their personal or application settings.",
      "Connection Status": "Logs the status of a user's connection, including times of connection and disconnection.",
      "Notification Interaction": "Records interactions with notifications, such as opening or dismissing them.",
      "Password Change": "Logs when a user changes their password, including the timestamp of the change.",
      "Account Creation": "Records the creation of a new user account, including details of the user and time of creation.",
      "Account Deletion": "Tracks the deletion of a user account, noting the time and reason for deletion if available.",
      "Role Assignment": "Logs changes to a user's role or permissions within the system.",
      "Profile Update": "Records updates made to a user's profile information, such as name, email, or profile picture.",
      "Two-factor Authentication Setup": "Logs the setup or changes to two-factor authentication settings for a user.",
      "Session Timeout": "Records instances of user sessions timing out due to inactivity."
}

log_dict_errors = {
      "Error Detected": "Logs the occurrence of an error within the system, including error code and description.",
      "Error Severity Level": "Records the severity level of the error (e.g., Info, Warning, Error, Critical).",
      "Stack Trace": "Provides the stack trace for the error, showing the point of failure in the code.",
      "Error Source Module": "Indicates the module or component within the system where the error originated.",
      "User Impact": "Describes the impact of the error on the end-user or system operation.",
      "Error Timestamp": "Records the exact date and time when the error occurred.",
      "Recovery Action": "Logs any actions taken by the system to recover from the error or mitigate its effects.",
      "Administrator Notification": "Indicates whether the system administrator or relevant personnel were notified of the error.",
      "Error Frequency": "Tracks how often the error occurs, useful for identifying recurring issues.",
      "Resolution Status": "Details the current status of the error, whether it has been resolved, is in progress, or pending investigation."
}

log_dict_error_codes = {
      "404 Not Found": "Logs when a requested resource could not be found on the server. Commonly occurs when a URL is mistyped or a page has been removed.",
      "500 Internal Server Error": "Indicates a generic error message when the server encounters an unexpected condition that prevents it from fulfilling the request.",
      "403 Forbidden": "Logged when the server understands the request but refuses to authorize it. This can be due to lack of access rights to the resource.",
      "401 Unauthorized": "Occurs when authentication is required and has failed or has not been provided yet.",
      "400 Bad Request": "Indicates that the server cannot or will not process the request due to a client error (e.g., malformed request syntax).",
      "502 Bad Gateway": "Logged when the server, while acting as a gateway or proxy, received an invalid response from the upstream server.",
      "503 Service Unavailable": "Indicates that the server is not ready to handle the request, typically due to temporary overloading or maintenance.",
      "408 Request Timeout": "Occurs when the server times out waiting for the request from the client.",
      "504 Gateway Timeout": "Logged when the server, while acting as a gateway or proxy, did not receive a timely response from the upstream server.",
      "410 Gone": "Indicates that the resource requested is no longer available and will not be available again.",
      "405 Method Not Allowed": "Occurs when a request method is not supported for the requested resource.",
      "406 Not Acceptable": "Logged when the server cannot produce a response matching the list of acceptable values defined in the request's proactive content negotiation headers.",
      "412 Precondition Failed": "Indicates that one or more conditions in the request header fields evaluated to false.",
      "413 Payload Too Large": "Occurs when the request entity is larger than limits defined by server; the server might close the connection or return a Retry-After header field.",
      "429 Too Many Requests": "Logged when the user has sent too many requests in a given amount of time ('rate limiting')."
}

# Log Severity level for random generator
log_dict_severity_level = {
      "NORMAL" : "An indication that the action is behaving normally.",
      "INFO": "General information about system operation. Indicates normal operation and useful operational information.",
      "DEBUG": "Detailed information, typically of interest only when diagnosing problems or troubleshooting.",
      "WARNING": "An indication of potential issues or changes in normal operation that doesn't necessarily indicate an error.",
      "ERROR": "A significant problem within the system that indicates a failure in a primary function.",
      "CRITICAL": "A severe condition indicating a critical failure in the system, often requiring immediate attention."
}
# Log Statuses for random generator
log_dict_status_nonissue = {
      "Pending": "Indicates that a task or process has been initiated but is not yet complete.",
      "In Progress": "Shows that the task or process is currently underway.",
      "Completed Successfully": "Signifies that the task or process has finished and met its expected outcome without errors.",
      "Queued": "Indicates that the task or process is waiting in a queue for execution."
}

log_dict_status_issue = {
      "Failed": "Indicates that the task or process did not complete successfully, often due to errors or exceptions.",
      "Warning": "Suggests that the task or process encountered some issues but was able to complete. Warnings often highlight situations that might require attention but are not critical failures.",
      "Cancelled": "This status is used when a task or process has been intentionally stopped before completion.",
      "Timed Out": "Used when a task or process does not complete within a specified time limit."
}

# Log Source for random generator
log_dict_source = {
      "Application": "Log entries originating from various parts of an application.",
      "System": "Logs generated by the underlying operating system.",
      "User": "Actions performed by users that generate logs.",
      "Network": "Logs originating from network activities, such as requests, responses, or connectivity issues.",
      "Database": "Logs generated from database operations, like queries or transactions.",
      "External Service": "Logs from interactions with external services or APIs.",
      "Device": "Logs generated by specific hardware devices (like printers, scanners, etc.).",
      "Security System": "Logs related to security events, like access control or breach attempts.",
      "Scheduler": "Logs originating from scheduled tasks or cron jobs.",
      "Error Handler": "Logs specifically related to error detection and handling."
}
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Log Functions for Generator                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

# Generate the Log ID field
def generate_log_id_field(num_records, len_id_char = 9):
      """
      Generate a list of unique log IDs with a specified character length.
      :param num_records: Number of log IDs to generate.
      :param len_id_char: Length of each log ID in characters (default is 9).
      :return: List of log IDs.
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

# Generate the Log Time Stamp field
def generate_log_timestamp_field(num_records, min_date = datetime(2010,1,1), max_date = datetime.now()):
      """
      Generate a list of timestamps for log entries within a specified date range.
      :param num_records: Number of timestamps to generate.
      :param min_date: Minimum date for the range.
      :param max_date: Maximum date for the range.
      :return: List of timestamps.
      """
      min_date = gtsf.function_date_int_to_datetime(min_date)
      max_date = gtsf.function_date_int_to_datetime(max_date)
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_date(min_date, max_date))
      return dict_list

# Generate the Log User ID field
def generate_log_userid_field(num_records, min_dig_id = 1, max_dig_id = 100000):
      """
      Generate a list of user IDs for log entries.
      :param num_records: Number of user IDs to generate.
      :param min_dig_id: Minimum value for user ID.
      :param max_dig_id: Maximum value for user ID.
      :return: List of user IDs.
      """
      dict_list = []
      for _ in range(num_records):
            temp_dig_id = str(random.randint(min_dig_id,max_dig_id))
            zero_count = len(str(max_dig_id))-len(temp_dig_id)
            dict_list.append("U" + "0"*zero_count + temp_dig_id)
      return dict_list

# Generate the Log IP Address Field
def generate_log_ip_address_field(num_records):
      """
      Generate a list of IP addresses for log entries.
      :param num_records: Number of IP addresses to generate.
      :return: List of IP addresses.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_log_ip_address())
      return dict_list

# Generate the Log Hostname field
def generate_log_hostname_field(num_records):
      """
      Generate a list of hostnames for log entries.
      :param num_records: Number of hostnames to generate.
      :return: List of hostnames.
      """
      dict_list = []
      for _ in range(num_records):
            dict_list.append(gtsf.generate_log_hostname())
      return dict_list

# Generate the Log Severity Level field
def generate_log_severity_field(num_records, priority_item = 'NORMAL', weight_main = 10, weight_oth = 1):
      """
      Generate a list of severity levels for log entries with weighted preference for a specific level.
      :param num_records: Number of severity levels to generate.
      :param priority_item: Severity level to prioritize (default 'NORMAL').
      :param weight_main: Weight for the prioritized severity level (default 10).
      :param weight_oth: Weight for other severity levels (default 1).
      :return: List of severity levels.
      """
      dict_list = []
      sev_list = list(log_dict_severity_level.keys())
      for _ in range(num_records):
            dict_list.append(gtsf.generate_random_unique_weighted_list(sev_list, priority_item, weight_main, weight_oth))
      return dict_list

# Generate the Log Status  field
def generate_log_status_field(num_records, severity_list):
      """
      Generate a list of statuses for log entries based on the severity level.
      :param num_records: Number of statuses to generate.
      :param severity_list: List of severity levels associated with each status.
      :return: List of statuses.
      """
      dict_list = []
      status_nonissue_list = list(log_dict_status_nonissue.keys())
      status_issue_list = list(log_dict_status_issue.keys())
      for x in range(num_records):
            if severity_list[x] == "NORMAL" or severity_list[x] == "INFO":
                  dict_list.append(random.choice(status_nonissue_list))
            else:
                  dict_list.append(random.choice(status_issue_list))
      return dict_list

# Generate the Log Reference ID field
def generate_log_referenceid_field(num_records, min_dig_id = 1, max_dig_id = 100000):
      """
      Generate a list of reference IDs for log entries.
      :param num_records: Number of reference IDs to generate.
      :param min_dig_id: Minimum value for reference ID.
      :param max_dig_id: Maximum value for reference ID.
      :return: List of reference IDs.
      """
      dict_list = []
      for _ in range(num_records):
            temp_dig_id = str(random.randint(min_dig_id,max_dig_id))
            zero_count = len(str(max_dig_id))-len(temp_dig_id)
            dict_list.append("R" + "0"*zero_count + temp_dig_id)
      return dict_list

# Generate the Log Module field
def generate_log_source_field(num_records):
      """
      Generate a list of sources for log entries.
      :param num_records: Number of sources to generate.
      :return: List of sources.
      """
      dict_list = []
      list_source = list(log_dict_source.keys())
      for _ in range(num_records):
            dict_list.append(random.choice(list_source))
      return dict_list

# Generate the Log Event Fields
def generate_log_event_fields(num_records):
      """
      Generate lists of log events and their descriptions.
      :param num_records: Number of log events to generate.
      :return: Two lists, one for log events and one for their descriptions.
      """
      dict_list_event = []
      dict_list_desc = []
      list_event = list(log_dict_event.keys())
      for x in range(num_records):
            temp_key = random.choice(list_event)
            dict_list_event.append(temp_key)
            dict_list_desc.append(log_dict_event[temp_key])
      return dict_list_event, dict_list_desc

# Generate the Log Data Change Fields
def generate_log_datachange_fields(num_records):
      """
      Generate lists of data change events and their descriptions.
      :param num_records: Number of data change events to generate.
      :return: Lists for data change events, descriptions, old values, and new values.
      """
      dict_list_event = []
      dict_list_desc = []
      list_dc = list(log_dict_data_change.keys())
      list_old = []
      list_new = []
      for x in range(num_records):
            temp_key = random.choice(list_dc)
            dict_list_event.append(temp_key)
            dict_list_desc.append(log_dict_data_change[temp_key])
            list_new.append("--New value--")
            list_old.append("--Old value--")
      return dict_list_event, dict_list_desc, list_old, list_new

# Generate the Log File Change Fields
def generate_log_filechange_fields(num_records):
      """
      Generate lists of file change events and their descriptions.
      :param num_records: Number of file change events to generate.
      :return: Lists for file change events, descriptions, old values, and new values.
      """
      dict_list_event = []
      dict_list_desc = []
      list_fc = list(log_dict_file_change.keys())
      list_old = []
      list_new = []
      for x in range(num_records):
            temp_key = random.choice(list_fc)
            dict_list_event.append(temp_key)
            dict_list_desc.append(log_dict_file_change[temp_key])
            list_new.append("--New value--")
            list_old.append("--Old value--")
      return dict_list_event, dict_list_desc, list_old, list_new

# Generate the Log Security Fields
def generate_log_security_fields(num_records):
      """
      Generate lists of security events and their descriptions.
      :param num_records: Number of security events to generate.
      :return: Two lists, one for security events and one for their descriptions.
      """
      dict_list_event = []
      dict_list_desc = []
      list_sec = list(log_dict_security.keys())
      for x in range(num_records):
            temp_key = random.choice(list_sec)
            dict_list_event.append(temp_key)
            dict_list_desc.append(log_dict_security[temp_key])
      return dict_list_event, dict_list_desc

# Generate the Log User Web Activity Fields
def generate_log_user_web_fields(num_records):
      """
      Generate lists of user web activities and their descriptions.
      :param num_records: Number of user web activities to generate.
      :return: Two lists, one for user web activities and one for their descriptions.
      """
      dict_list_event = []
      dict_list_desc = []
      list_u = list(log_dict_user_web.keys())
      for x in range(num_records):
            temp_key = random.choice(list_u)
            dict_list_event.append(temp_key)
            dict_list_desc.append(log_dict_user_web[temp_key])
      return dict_list_event, dict_list_desc

# Generate the Log User Server Activity Fields
def generate_log_user_server_fields(num_records):
      """
      Generate lists of user server activities and their descriptions.
      :param num_records: Number of user server activities to generate.
      :return: Two lists, one for user server activities and one for their descriptions.
      """
      dict_list_event = []
      dict_list_desc = []
      list_u = list(log_dict_user_server.keys())
      for x in range(num_records):
            temp_key = random.choice(list_u)
            dict_list_event.append(temp_key)
            dict_list_desc.append(log_dict_user_server[temp_key])
      return dict_list_event, dict_list_desc
            
# Generate the Log User Account Activity Fields
def generate_log_user_account_fields(num_records):
      """
      Generate lists of user account activities and their descriptions.
      :param num_records: Number of user account activities to generate.
      :return: Two lists, one for user account activities and one for their descriptions.
      """
      dict_list_event = []
      dict_list_desc = []
      list_u = list(log_dict_user_accout.keys())
      for x in range(num_records):
            temp_key = random.choice(list_u)
            dict_list_event.append(temp_key)
            dict_list_desc.append(log_dict_user_accout[temp_key])
      return dict_list_event, dict_list_desc
                    
# Generate the Log Error Activity Fields
def generate_log_errors_fields(num_records):
      """
      Generate lists of error events and their descriptions.
      :param num_records: Number of error events to generate.
      :return: Two lists, one for error events and one for their descriptions.
      """
      dict_list_event = []
      dict_list_desc = []
      list_u = list(log_dict_errors.keys())
      for x in range(num_records):
            temp_key = random.choice(list_u)
            dict_list_event.append(temp_key)
            dict_list_desc.append(log_dict_errors[temp_key])
      return dict_list_event, dict_list_desc

# Generate the Log Error Activity Fields
def generate_log_error_codes_fields(num_records):
      """
      Generate lists of error code events and their descriptions.
      :param num_records: Number of error code events to generate.
      :return: Two lists, one for error code events and one for their descriptions.
      """
      dict_list_event = []
      dict_list_desc = []
      list_u = list(log_dict_error_codes.keys())
      for x in range(num_records):
            temp_key = random.choice(list_u)
            dict_list_event.append(temp_key)
            dict_list_desc.append(log_dict_error_codes[temp_key])
      return dict_list_event, dict_list_desc
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------              Generate the Log Table                     ---------- 
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

def generate_table_log_general(dict, id_field_name = 'ID_Record'): 
      """
      Populate a dictionary with various general log data fields to build a log table.
      :param dict: Dictionary to populate with log data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with general log data fields.
      """
      num_records = len(dict[id_field_name])
      dict['Log ID'] = generate_log_id_field(num_records)
      dict['Time Stamp'] = generate_log_timestamp_field(num_records)
      dict['User ID'] = generate_log_userid_field(num_records)
      dict['IP Address'] = generate_log_ip_address_field(num_records)
      dict['Hostname'] = generate_log_hostname_field(num_records)
      dict['Log Level'] = generate_log_severity_field(num_records)
      dict['Status'] = generate_log_status_field(num_records, dict['Log Level'])
      dict['Reference ID'] = generate_log_referenceid_field(num_records)
      dict['Source'] = generate_log_source_field(num_records)
      dict['Log Event'], dict['Log Event Description']  = generate_log_event_fields(num_records)
      return dict

def generate_table_log_datachange(dict, id_field_name = 'ID_Record'):  
      """
      Populate a dictionary with log data fields related to data changes.
      :param dict: Dictionary to populate with log data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with log data fields related to data changes.
      """
      num_records = len(dict[id_field_name])
      dict['Log ID'] = generate_log_id_field(num_records)
      dict['Time Stamp'] = generate_log_timestamp_field(num_records)
      dict['User ID'] = generate_log_userid_field(num_records)
      dict['IP Address'] = generate_log_ip_address_field(num_records)
      dict['Hostname'] = generate_log_hostname_field(num_records)
      dict['Log Level'] = generate_log_severity_field(num_records)
      dict['Status'] = generate_log_status_field(num_records, dict['Log Level'])
      dict['Reference ID'] = generate_log_referenceid_field(num_records)
      dict['Source'] = generate_log_source_field(num_records)
      dict['Log Data Change'], dict['Log Data Change Description'], dict['Old Value'], \
      dict['New Value'] = generate_log_datachange_fields(num_records)
      return dict

def generate_table_log_filechange(dict, id_field_name = 'ID_Record'):  
      """
      Populate a dictionary with log data fields related to file changes.
      :param dict: Dictionary to populate with log data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with log data fields related to file changes.
      """
      num_records = len(dict[id_field_name])
      dict['Log ID'] = generate_log_id_field(num_records)
      dict['Time Stamp'] = generate_log_timestamp_field(num_records)
      dict['User ID'] = generate_log_userid_field(num_records)
      dict['IP Address'] = generate_log_ip_address_field(num_records)
      dict['Hostname'] = generate_log_hostname_field(num_records)
      dict['Log Level'] = generate_log_severity_field(num_records)
      dict['Status'] = generate_log_status_field(num_records, dict['Log Level'])
      dict['Reference ID'] = generate_log_referenceid_field(num_records)
      dict['Source'] = generate_log_source_field(num_records)
      dict['Log File Change'], dict['Log File Change Description'], dict['Old Value'], \
      dict['New Value'] = generate_log_filechange_fields(num_records)
      return dict

def generate_table_log_security(dict, id_field_name = 'ID_Record'):  
      """
      Populate a dictionary with log data fields related to security events.
      :param dict: Dictionary to populate with log data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with log data fields related to security events.
      """
      num_records = len(dict[id_field_name])
      dict['Log ID'] = generate_log_id_field(num_records)
      dict['Time Stamp'] = generate_log_timestamp_field(num_records)
      dict['User ID'] = generate_log_userid_field(num_records)
      dict['IP Address'] = generate_log_ip_address_field(num_records)
      dict['Hostname'] = generate_log_hostname_field(num_records)
      dict['Log Level'] = generate_log_severity_field(num_records)
      dict['Status'] = generate_log_status_field(num_records, dict['Log Level'])
      dict['Reference ID'] = generate_log_referenceid_field(num_records)
      dict['Source'] = generate_log_source_field(num_records)
      dict['Log Security'], dict['Log Security Description'] = generate_log_security_fields(num_records)
      return dict

# Log Table Generator: user web activity
def generate_table_log_user_web_activity(dict, id_field_name = 'ID_Record'):  
      """
      Populate a dictionary with log data fields related to user web activity.
      :param dict: Dictionary to populate with log data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with log data fields related to user web activity.
      """
      num_records = len(dict[id_field_name])
      dict['Log ID'] = generate_log_id_field(num_records)
      dict['Time Stamp'] = generate_log_timestamp_field(num_records)
      dict['User ID'] = generate_log_userid_field(num_records)
      dict['IP Address'] = generate_log_ip_address_field(num_records)
      dict['Hostname'] = generate_log_hostname_field(num_records)
      dict['Log Level'] = generate_log_severity_field(num_records)
      dict['Status'] = generate_log_status_field(num_records, dict['Log Level'])
      dict['Reference ID'] = generate_log_referenceid_field(num_records)
      dict['Source'] = generate_log_source_field(num_records)
      dict['Log User Activity'], dict['Log User Description'] = generate_log_user_web_fields(num_records)
      return dict

# Log Table Generator: user server activity
def generate_table_log_user_server_activity(dict, id_field_name = 'ID_Record'):  
      """
      Populate a dictionary with log data fields related to user server activity.
      :param dict: Dictionary to populate with log data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with log data fields related to user server activity.
      """
      num_records = len(dict[id_field_name])
      dict['Log ID'] = generate_log_id_field(num_records)
      dict['Time Stamp'] = generate_log_timestamp_field(num_records)
      dict['User ID'] = generate_log_userid_field(num_records)
      dict['IP Address'] = generate_log_ip_address_field(num_records)
      dict['Hostname'] = generate_log_hostname_field(num_records)
      dict['Log Level'] = generate_log_severity_field(num_records)
      dict['Status'] = generate_log_status_field(num_records, dict['Log Level'])
      dict['Reference ID'] = generate_log_referenceid_field(num_records)
      dict['Source'] = generate_log_source_field(num_records)
      dict['Log User Activity'], dict['Log User Description'] = generate_log_user_server_fields(num_records)
      return dict

# Log Table Generator: user account activity
def generate_table_log_user_account_activity(dict, id_field_name = 'ID_Record'):  
      """
      Populate a dictionary with log data fields related to user account activity.
      :param dict: Dictionary to populate with log data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with log data fields related to user server activity.
      """
      num_records = len(dict[id_field_name])
      dict['Log ID'] = generate_log_id_field(num_records)
      dict['Time Stamp'] = generate_log_timestamp_field(num_records)
      dict['User ID'] = generate_log_userid_field(num_records)
      dict['IP Address'] = generate_log_ip_address_field(num_records)
      dict['Hostname'] = generate_log_hostname_field(num_records)
      dict['Log Level'] = generate_log_severity_field(num_records)
      dict['Status'] = generate_log_status_field(num_records, dict['Log Level'])
      dict['Reference ID'] = generate_log_referenceid_field(num_records)
      dict['Source'] = generate_log_source_field(num_records)
      dict['Log User Activity'], dict['Log User Description'] = generate_log_user_account_fields(num_records)
      return dict

# Log Table Generator: log errors
def generate_table_log_errors(dict, id_field_name = 'ID_Record'): 
      """
      Populate a dictionary with log data fields related to log errors.
      :param dict: Dictionary to populate with log data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with log data fields related to user server activity.
      """
      num_records = len(dict[id_field_name])
      dict['Log ID'] = generate_log_id_field(num_records)
      dict['Time Stamp'] = generate_log_timestamp_field(num_records)
      dict['User ID'] = generate_log_userid_field(num_records)
      dict['IP Address'] = generate_log_ip_address_field(num_records)
      dict['Hostname'] = generate_log_hostname_field(num_records)
      dict['Log Level'] = generate_log_severity_field(num_records)
      dict['Status'] = generate_log_status_field(num_records, dict['Log Level'])
      dict['Reference ID'] = generate_log_referenceid_field(num_records)
      dict['Source'] = generate_log_source_field(num_records)
      dict['Log Errors'], dict['Log Error Description'] = generate_log_errors_fields(num_records)
      return dict

# Log Table Generator: log error codes
def generate_table_log_error_codes(dict, id_field_name = 'ID_Record'):  
      """
      Populate a dictionary with log data fields related to log error codes.
      :param dict: Dictionary to populate with log data.
      :param num_records: Number of records to generate for each field.
      :return: Dictionary populated with log data fields related to user server activity.
      """
      num_records = len(dict[id_field_name])
      dict['Log ID'] = generate_log_id_field(num_records)
      dict['Time Stamp'] = generate_log_timestamp_field(num_records)
      dict['User ID'] = generate_log_userid_field(num_records)
      dict['IP Address'] = generate_log_ip_address_field(num_records)
      dict['Hostname'] = generate_log_hostname_field(num_records)
      dict['Log Level'] = generate_log_severity_field(num_records)
      dict['Status'] = generate_log_status_field(num_records, dict['Log Level'])
      dict['Reference ID'] = generate_log_referenceid_field(num_records)
      dict['Source'] = generate_log_source_field(num_records)
      dict['Log Error Code'], dict['Log Error Code Description'] = generate_log_error_codes_fields(num_records)
      return dict

#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------- 

# def generate_table_log(min_rand_record_lim = 1, max_rand_record_lim = 1000):
#       """
#       Generate a table of log data with random data.
#       :param min_rand_record_lim: Minimum limit for random record length.
#       :param max_rand_record_lim: Maximum limit for random record length.
#       :return: Dictionary representing the generated log table.
#       """
#       log_num_records = gtsf.generate_random_record_length(min_rand_record_lim, max_rand_record_lim)
#       log_data = gtsf.table_generate_id_records(log_num_records)
#       log_data = generate_table_log_datachange(log_data, log_num_records)
#       return log_data

