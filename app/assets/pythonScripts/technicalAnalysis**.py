import urllib2
import time
import datetime
import sys
stocks = sys.argv[1] 
import MySQLdb
from datetime import date

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='1234',
    db='investmentaidsys')

cursor = mydb.cursor()
def pullData():
    cursor.execute('TRUNCATE TABLE stock_historic_data;')
    mydb.commit()
    try:
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stocks+'/chartdata;type=quote;range=1y/csv'
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')
            
        for eachLine in splitSource:
            splitLine = eachLine.split(',')
            if len(splitLine) == 6:
                if 'values' not in eachLine:
                    now = datetime.datetime.now()
                    #d = datetime.datetime.strptime(splitLine[0], '%Y%m%d').strftime('%Y, %m, %d')
                    date=  splitLine[0] + ' 00:00:00'
                    dt = time.mktime(datetime.datetime.strptime(date, "%Y%m%d %H:%M:%S").timetuple())
                    v1= int(round(dt*1000))
                    v2 = splitLine[1]
                    v3 = splitLine[2]
                    v4 = splitLine[3]
                    v5= splitLine[4]
                    v6 = splitLine[5]
                   
                    cursor.execute('INSERT INTO stock_historic_data(stock_tickers,price_date,price_close,price_high,price_low ,price_open,volume,updated_at)' \
                              ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(stock,v1,v2,v3,v4,v5,v6,now))

        print 'Pulled '+ stock
        print 'sleeping'
        time.sleep(5)   
        mydb.commit()
        cursor.close()
        print "Done"
        
    except Exception ,e:
        print 'main loop',str(e)

pullData()


