"""

   This moduel contains a group of functions found useful is using Python
   pandas with csv and xlsx file.

   Functions define here


        def create_dataframe_file_from_csv(csv_file_path, **options):
        def create_xlsx_file_from_df(dataframe, xlsx_file_path, sheet_name=None):
        def create_xlsx_file_from_csv(csv_file_path, xlsx_file_path, **options):
        def csv_concat(source_files, destination_file):
        def create_csv_file_from_xlsx(xlsx_file_path, csv_file_path, csv_headers=True, **options):
        def convert_to_time_period(source_file, date_column_name, time_period):

   Individual functions are documented in their docstrings.

   The work is in the public domain and comes with no warrenty of fitness for any purpose.
   
   The work was create for classroom exposition. 

   DO NOT USE THESE WITHOUT EXTENSIVE TESTING

"""

from pandas import DataFrame, Series
import pandas as pd
import os
import glob


def create_dataframe_file_from_csv(csv_file_path, **options):
    """
        Name: create_dataframe_file_from_csv

	Function: Read a csv file and convert it to a panda dataframe

	Return: A single DataFrame

	Options
	   csv_file_path: is the path to a csv file to be 
	                  used to create a panda DataFrame 

           **options: This is a list of key-value pairs 
	              (key:value) which are used to describe 
		      the csv file and how it is to be imported into
		      Python

		      Options
		         header=<row index of column names>
			 index_col=<index of column with row names>
			 skiprows=<number of row to skip at start of csv file>
			 names=<list of the new column names>
			 usecols=<list of colums to be returned from csv file>
			 csv_headers=<True/False to have or not have column names>

        Examples

            - column names and data, no index column: 

               create_dataframe_file_from_csv( "Source_files/google.csv', header=0)
	       
	            - index_col default is None

            - only data:

               create_dataframe_file_from_csv( "Source_files/google.csv', csv_headers=False, header=None, skiprows=1 )
	             
                   - Assumes only 1 row of column headers	

            - new column names: 

               create_dataframe_file_from_csv( "Source_files/google.csv', header=None, skiprows=1, name=['d', 'o', 'h', 'l', 'c', 'v'])
	             
                   - Assumes only 1 row of column headers	


            - select columns: 'header=0, index_col=None, usecols=[]'

               create_dataframe_file_from_csv( "Source_files/google.csv", header=0, usecols=["open", "high"])


    """

    import pandas as pd
    
    options_passed = dict(options)
    
    df = pd.read_csv(csv_file_path, **options_passed)
    return df
        

def create_xlsx_file_from_df(dataframe, xlsx_file_path, sheet_name=None):
    """
        Name: create_xlsx_file_from_df

	Function: Create an .xlsx fine from a panda DataFrame

	Return: None
	    The file is written out to the file path

	Options
	    sheet_name=<name on tab in workbook>

        Examples
           - write out a dataframe, Source_files/google.csv to xlsx file, Destination_files/google.xlsx, with a tab of "google"

	      create_xlsx_file_from_df("./Source_files/google.csv", "Destination_files/google.xlsx", sheet_name="Google")
    """

    import pandas as pd
    
    writer = pd.ExcelWriter(xlsx_file_path)
    
    if not sheet_name:
        dataframe.to_excel(writer)
    else:
        dataframe.to_excel(writer, sheet_name = sheet_name)
    writer.save()
    return

def create_xlsx_file_from_csv(csv_file_path, xlsx_file_path, **options):
    """
        Name: create_xlsx_file_from_csv

	Function: Create a xlsx file from a csv file

	Return: None
	   The xlsx file is created in the file system

	Options
	   csv_file_path: is the path to a csv file to be 
	                  used to create a panda DataFrame 

	   xlsx_file_path: pathname to location to store xlsx file

           **options: This is a list of key-value pairs 
	              (key:value) which are used to describe 
		      the csv file and how it is to be imported into
		      Python

		      Options
		         header=<row index of column names>
			 index_col=<index of column with row names>
			 skiprows=<number of row to skip at start of csv file>
			 names=<list of the new column names>
			 usecols=<list of colums to be returned from csv file>
			 csv_headers=<True/False to have or not have column names>

        Examples

            - column names and data, no index column: 

               create_xlsx_file_from_csv( "Source_files/google.csv", "Destination_files/google.xlsx",  header=0)
	       
	            - index_col default is None

            - only data:

               create_xlsx_file_from_csv( "Source_files/google.csv", 
	                                  "Destination_files/google.xlsx",  
					  csv_headers=False, header=None, skiprows=1 )
	             
                   - Assumes only 1 row of column headers	

            - new column names: 

               create_xlsx_file_from_csv( "Source_files/google.csv",  
	                                  "Destination_files/google.xlsx", 
					  header=None, skiprows=1, name=['d', 'o', 'h', 'l', 'c', 'v'])
	             
                   - Assumes only 1 row of column headers	


            - select columns: 'header=0, index_col=None, usecols=[]'

               create_xlsx_file_from_csv( "Source_files/google.csv",  
	                                  "Destination_files/google.xlsx", 
					  header=0, usecols=["open", "high"])


    """

    import pandas as pd
    
    options_passed = dict(options)
    sheet_name = options.get('sheet_name')
    if sheet_name:
        options_passed.pop('sheet_name')
    
    df = create_dataframe_file_from_csv(csv_file_path, **options_passed)
    
    if not sheet_name:
        create_xlsx_file_from_df(df, xlsx_file_path, sheet_name = sheet_name)
    else:
        create_xlsx_file_from_df(df, xlsx_file_path)
    return
    

def csv_concat(source_files_regex, destination_xlsx_file):
    """
        Name: csv_concat(source_files, destination_file)

	Function: creates a single xlsx file from multiple
	          csv files. The csv files must have the 
		  same column names and all files must reside
		  in the same directory

	Return: None

	Options
	
	    source_files_regex: a regular expression matching
	                        the files to be concatenated
	    
	    destination_xlsx_file: the path to the xlsx file

        Example

	    csv_concat(r'Source_files/google_20*.csv', 
	               'Destination_files/multiple_sources.xlsx')

    """

    first = True
    for csvfile in glob.glob(os.path.join('.', source_files_regex)):
        temp_df = pd.read_csv(csvfile, index_col = False)
    
        if first:
            final_df = DataFrame(columns = temp_df.columns)
            first = False
        
        final_df = pd.concat([final_df, temp_df], ignore_index = True, axis = 0)
    
    final_df.sort_values(by = ['date'], axis = 0, inplace = True)

    create_xlsx_file_from_df(final_df, destination_xlsx_file)    

    return

def csv_concat_list(source_files, destination_xlsx_file):
    """
        Name: csv_concat(source_files, destination_file)

	Function: creates a single xlsx file from multiple
	          csv files. The csv files must have the 
		  same column names and all files must reside
		  in the same directory

	Return: None

	Options
	
	    source_files: list of csv file
	    
	    destination_xlsx_file: the path to the xlsx file

        Example

	    csv_concat_list(location.txt, 
	               'Destination_files/multiple_sources.xlsx')

    """

    first = True
    for csvfile in source_files:
        temp_df = pd.read_csv(csvfile, index_col=False)
    
        if first:
            final_df = DataFrame(columns = temp_df.columns)
            first = False
        
        final_df = pd.concat([final_df, temp_df], ignore_index = True, axis = 0)
    
    final_df.sort_values(by = ['date'], axis = 0, inplace = True)

    create_xlsx_file_from_df(final_df, destination_xlsx_file)    

    return

def create_csv_file_from_xlsx(xlsx_file_path, csv_file_path, csv_headers = True, **options):
    """
        Name: create_csv_file_from_xlsx(xlsx_file_path, 
	                                csv_file_path, 
					csv_headers=True, 
					**options)

	Function: Create a csv file from an xlsx file

	Return:  None

	Options
	   xlsx_file_path: xlsx file to convert to csv file

	   csv_file_path: is the path to a csv file to be 
	                  used to create a panda DataFrame 

           csv_header: Boolean flag defaulted to True 
	               True means column names included in csv file
		       Flase means no column headers
	       
           **options: This is a list of key-value pairs 
	              (key:value) which are used to describe 
		      the csv file and how it is to be exported into
		      Python

		      Options
		         header=<row index of column names>
			 index_col=<index of column with row names>
			 skiprows=<number of row to skip at start of csv file>
			 names=<list of the new column names>
			 usecols=<list of colums to be returned from csv file>
			 csv_headers=<True/False to have or not have column names>

        Examples

            - only data:

	       create_csv_file_from_xlsx("google_all.xlsx", "google_just_data.csv", 
                          csv_headers=False, header=None, skiprows=1, index_col=0)

                   - Assumes only 1 row of column headers	

            - select columns: 'header=0, index_col=None, usecols=[]'

	       create_csv_file_from_xlsx("google_all.xlsx", "google_open_close.csv", 
                header=0, index_col=None, usecols=['date', 'open','close'])

    """

    def create_csv_file_from_xlsx(xlsx_file_path, csv_file_path, csv_headers = True, **options):
        from pandas import DataFrame, Series
        import pandas as pd

        options_passed = dict(options)
    
        df = pd.read_excel(xlsx_file_path, **options_passed)
    
        if csv_headers:
            df.to_csv(csv_file_path, index = False)
        else:
            df.to_csv(csv_file_path, index = False, header = False)

        return


def convert_to_time_period(source_file, date_column_name, time_period):
    """
	Function: convert_to_time_period(source_file, date_column_name, time_period)

	Return: Creates a DataFrame with index of a time period. Uses a date field in 
	        the csv file. Date field is removed after index is created

	Options

	    source_file: path to csv file in which date is a string.  The date field 
	                 is converted to a period field specified in the time_period 
			 example.

	    date_column_name: name of the field containing the date column.

	    time_period: code specified as a string for specifying the time period
	    
	        D: day
		M: month
		Y: year

        Examples

	df_google_year = convert_to_day_period("./Source_files/GOOGLE_stock.csv", 
	                                       "date", "Y")

    """

    import pandas as pd
    
    df = pd.read_csv(source_file)
    
    df_date_index = df.rename(index = pd.to_datetime(df[date_column_name], 
                              format = '%Y-%m-%d')).drop(date_column_name, axis = 1)
    
    df_day_all_days = \
         df_date_index.resample(time_period, kind = 'period').mean().fillna(method = 'ffill')
    
    return df_day_all_days
    
