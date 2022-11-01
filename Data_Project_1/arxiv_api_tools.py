import api_functions
import urllib, urllib.request

name = str(input("What topic do you want to search? "))
count = input("How many results do you want? ")
query = urllib.parse.quote(name)
count1 = urllib.parse.quote(count)
query1= 'all:' + query
url = 'http://export.arxiv.org/api/query?search_query='+query1+'&start=0&max_results='+count1
root = api_functions.select_data(url)

'''
This section answers: 
Convert the general format and data structure of the data source (from
JSON to CSV, from CSV to JSON, from JSON into a SQL database table,
etc. I want the option to convert any source to any target. So, if I get a
CSV as an input, I want the user to choose an output

Each of the following options allows the user to save the files to their local disk

Afterwards the number of columns and rows gets printed out.
'''
option = str(input("What do you want as an output? type: sql, csv, or json) "))
s = ['sql', 'SQL', 'Sql']
c = ['csv', 'CSV', 'Csv']
j = ['json', 'JSON', 'Json']
valid_input = False
while valid_input == False:
    if option in s: # User wants sql output
        api_functions.data_to_sql(name, root)
        valid_input = True
    elif option in c: # User wants csv output
        api_functions.data_to_csv(name, root)
        valid_input = True
    elif option in j: # User wants json output
        api_functions.data_to_json(name, root)
        valid_input = True
    else:
        print("Invalid Input") # Try again