# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
pip install requests
pip install config
import requests
pip install psycopg2 
import psycopg2 #this package is used for data transfer to postgres
import pandas as pd

import config
#first tried the datacamp video tutorial to access data by calling an api
#HOST = "https://api.census.gov/data"
#year = "2019"
#dataset = "/acs/acs5"
#base_url = "/".join([HOST,year,dataset])

#predicates ={}
#get_vars= ["AIRES","B01001B_001E","B01001_002E","B20005I_060E","B20005I_061E"]

#predicates["get"] = ",".join(get_vars)
#predicates["for"] = "state:*"

#predicates["for"] = "block%20group:1&in=state:01%20county:001%20tract:020100"
#predicates didn't work when trying to access block level

#switched to tutorial from the census wesbite
v = "https://api.census.gov/data/2019/acs/acs5?get=B01001_001E,B01001_002E,B01001_026E&for=block%20group:*&in=state:02&in=county:*&in=tract:*"

r = requests.get(v)

print(r.json()[0])

print(r.text)

#importing data 

#this method is from the datacamp tutorial

col_names = ["TotalPopulation","Total Males By Age","Total Females by Age","state","county","tract","block group"]

df = pd.DataFrame(columns = col_names, data= r.json()[1:])

#exporting data to a csv

df.to_csv('D:\Kumar\CMU Course\CMU Course\Fall 21\94889 MLPP\ACS5.csv')



#making the connection
conn = psycopg2.connect(host= "acs-db.mlpolicylab.dssg.io",port= 5432,user= "**",database= "acs_data_loading",password= "**")#removed password and username for privacy

#now creating a table with the same name
#first creating a cursor so as to excute the commands
cur = conn.cursor()

cur.execute("""CREATE TABLE ACS5Kumar(Index integer,TotalPop integer,TotalMPop integer,TotalFPop integer, state integer,county integer,tract integer,blockgroup integer)""")
conn.commit()

#this version is a smaller version of the copying data
#Notice that we don't need the `csv` module.
# Skip the header row.
#with open('D:\Kumar\CMU Course\CMU Course\Fall 21\94889 MLPP\ACS5.csv', 'r') as f:next(f) cur.copy_from(f, 'ACS5Kumar', sep=',')
    

with open('D:\Kumar\CMU Course\CMU Course\Fall 21\94889 MLPP\ACS5.csv', 'r') as f:
    reader = csv.reader(f) 
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute("""INSERT INTO ACS5Kumar VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",row)

conn.commit()


#need to run this at the end 






