import MySQLdb
import pandas as pd
import csv
import datetime

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='investmentaidsys')
cursor = mydb.cursor()

files= open('stocks.csv')
csvfile = csv.reader(x.replace('NaN',"") for x in files) ## change blank row into string
intoList=map(tuple,csvfile)

cursor.execute('TRUNCATE TABLE company;')
mydb.commit()
    
for each in intoList:
    splitline = each
    if each:# check if row empty
        if 'Ticker' not in each:
         
            now = datetime.datetime.now()
            v1=splitline[0]
            v2=splitline[1]
            v3=splitline[2]  
            v4=splitline[3]  
          
            cursor.execute('INSERT INTO company(company_name,stock_tickers,enchange_sym,company_industry,created_at,updated_at)' \
                          ' VALUES(%s,%s,%s,%s,%s,%s)',(v2,v1,v3,v4,now,now))
            
            print 'insert into db'
            mydb.commit()


    
cursor.close()
    
