import pandas as pd

class Statistics:
    def __init__(self, df):
        self.df = df
        
    def list_unique_values(self, field_name):
        """
        List all unique values in a specified field of the dataset.

        :param field: The field name whose unique values are to be listed.
        :return: A set of unique values in the specified field.
        """
        unique_values = set()
        for record in self.df[field_name]:
            if record not in unique_values:
                unique_values.add(record)
        return unique_values
        
    def count_values_field_dict(self, list_to_count, field):
        """
        Count how many times each value occurs in a specified field of a dataset.

        :param data: A list of dictionaries representing the dataset.
        :param field: The field name for which to count the occurrences.
        :return: A dictionary with values as keys and their occurrence counts as values.
        """
        value_counts = {}
        for list in list_to_count:
            value_counts[list] = 0
            for record in self.df[field]:
                if list == record:
                    value_counts[list] += 1
        return value_counts
    
    def count_values_field(self, field_name):
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")
        return self.df[field_name].value_counts()
    

    
    def count_nulls_in_field(self, field_name):
        """
        Count the number of null (NaN) values in a specific field of a DataFrame.

        :param df: pandas DataFrame
        :param field_name: Name of the field (column) in which to count nulls
        :return: Number of null values in the specified field
        """
        if field_name not in self.df.columns:
            raise ValueError(f"Field '{field_name}' not found in DataFrame.")

        null_count = self.df[field_name].isnull().sum()
        return null_count
    
    def count_nulls_in_all_fields(self):
        """
        Count the number of null (NaN) values in each field of a DataFrame and summarize in a dictionary.

        :param df: pandas DataFrame
        :return: Dictionary with field names as keys and number of null values as values
        """
        null_counts = {}
        for field in self.df.columns:
            null_count = self.df[field].isnull().sum()
            null_counts[field] = null_count
        return null_counts
    
    def data_view(self):
        # Viewing the first few rows
        print(' ')
        print('...Data Info:')
        print(self.df.info())
        # Basic statistical details
        print(' ')
        print('...Data Description:')
        print(self.df.describe())


# how many active/closed
    
# """
# Detect outliers in a specified numerical column using Z-scores.
# - Parameter column: The column to check for outliers.
# - Flags rows where the column's value is an outlier (Z-score > 3).
# """
# if self.df[column].dtype in ['int64', 'float64']:
#     from scipy import stats
#     outliers = self.df[(np.abs(stats.zscore(self.df[column])) > 3)]
#     if not outliers.empty:
#         print("Outliers found in {}:\n".format(column), outliers)
