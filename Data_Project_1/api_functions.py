import urllib, urllib.request
try:
    import requests
except ImportError:
    print("Missing requests, try pip install requests")
    exit()
from xml.dom import minidom
import json
from datetime import datetime, timedelta
try:
    import pandas as pd
except ImportError:
    print("Missing pandas, try pip install pandas")
    exit()
import sqlite3
def select_data(url):
    '''
    This function answers: 
    Fetch / download / retrieve a remote data file by URL (API call like we did
    in class)
    '''
    response = requests.get(url)
    root = minidom.parseString(response._content)
    return root

def add_data_to_list(root):
    '''
    takes selected data and formats it into a list so multiple papers can be added to a json

    This function answers:
    Modify the number of columns from the source to the destination,
    reducing or adding columns so that you transform it with something
    else…you can make up whatever it is…like date changes…or mash up
    two columns…it’s up to you.

    In this case I merge the Authors list into one and add the current time for when the data was pulled. 
    I also add a count column in front of the actual api data. 
    by the end of this function the data is stored 'close to' json format. 
    '''
    i = 0 # initalize count to 0
    data = [] # data list
    for entry in root.getElementsByTagName('entry'):
        temp = {}
        # Keep count of No. so elements can be acessed by index
        temp["No."] = i
        i = i + 1
        # The way I grab information is based on the example xml
        # Store internal id
        temp['internal_id'] = entry.getElementsByTagName('id')[0].firstChild.nodeValue.strip()
        # Store title
        temp['title'] = entry.getElementsByTagName('title')[0].firstChild.nodeValue.strip()
        # Store text 
        temp['text'] = entry.getElementsByTagName('summary')[0].firstChild.nodeValue.strip()
        # Store publication date
        temp['publication_date'] = entry.getElementsByTagName('published')[0].firstChild.nodeValue.strip()
        # Store author name
        temp['authors'] = []
        for author in entry.getElementsByTagName('author'):
            temp['authors'].append(author.getElementsByTagName('name')[0].firstChild.nodeValue.strip())
        # Append the temp dict to the data list
        # Time pulled 
        temp['Time Pulled'] = str(datetime.now())

        data.append(temp)
    return data

def data_to_json(title, root):
    '''
    Converts the data to Json
    '''
    data = add_data_to_list(root)
    with open(title.replace(" ", "_")+'.json', 'w') as json_file:
        json.dump(data, json_file) 
    print("This json file is {} by {}: ".format(len(data), len(data[0])))

def data_to_csv(title, root):
    '''
    Converts the data to csv
    '''
    title = title.replace(" ", "_")

    data = add_data_to_list(root)
    df = pd.DataFrame.from_dict(data)
    print("This csv is {} by {}: ".format(df.shape[0], df.shape[1]))
    return df.to_csv(title+".csv")

def data_to_sql(title, root):
    '''
    Converts the data to sqlite file
    '''
    title = title.replace(" ", "_")
    # create a db according to the title
    connection = sqlite3.connect(title+'.db')
    cursor = connection.cursor()

    # To prevent duplicate data I drop the table
    cursor.execute("DROP TABLE if exists "+ title.upper())

    cursor.execute('Create Table if not exists '+ title.upper() +' (No TEXT, internal_id TEXT, title TEXT, text TEXT,\
     publication_date TEXT, authors TEXT,Time Pulled TEXT)')

    # add data to the db
    data = add_data_to_list(root)
    columns = ['No.','internal_id','title', 'text', 'publication_date', 'authors', 'Time Pulled']
    for row in data:
        keys= tuple(str(row[c]) for c in columns)
        cursor.execute('insert into '+ title.upper() +' values(?,?,?,?,?,?,?)',keys)

    cursor.execute("SELECT COUNT(*) FROM "+ title.upper()) # number of rows
    result = cursor.fetchone()[0]
    cursor.execute("PRAGMA table_info("+title.upper()+")") # number of columns
    no_col = len(cursor.fetchall())
    print("This sql db is {} by {}: ".format(result, no_col))
    connection.commit()
    connection.close()


def print_sql_db(title):
    '''
    prints sql db according to the title
    '''
    title = title.replace(" ", "_")

    connection = sqlite3.connect(title+'.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM '+ title.upper() +';')
    all_results = cursor.fetchall()
    print(all_results)

