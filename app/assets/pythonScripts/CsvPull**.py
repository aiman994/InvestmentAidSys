import MySQLdb
import pandas as pd
import csv
import datetime

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='investmentaidsys')

cursor = mydb.cursor()

files= open('companylist(1).csv')
csvfile = csv.reader(x.replace('NaN',"") for x in files) ## change blank row into string
intoList=map(tuple,csvfile)

##cursor.execute('TRUNCATE TABLE company;')
##mydb.commit()
v7="NYSE"    
for each in intoList:
    splitline = each
    if each:# check if row empty
        if 'Symbol' not in each:
            now = datetime.datetime.now()
            v1=splitline[0]
            v2=splitline[1]
            v3=splitline[3]  
            v4=splitline[5]  
            v5=splitline[6]
            v6=splitline[7] 
            cursor.execute('INSERT INTO company(company_name,stock_tickers,exchange,company_industry,created_at,updated_at, company_sector,IPOyear,marketCap)' \
                          ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(v2,v1,v7,v6,now,now,v5,v4,v3))
            
            print 'insert into db'
            mydb.commit()


    
cursor.close()
    
