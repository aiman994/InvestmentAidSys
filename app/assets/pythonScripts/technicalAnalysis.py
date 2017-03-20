import urllib2
import time
import datetime
import sys
stocks = sys.argv[1] 
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='investmentaidsys')

cursor = mydb.cursor()
def pullData(stock):
    
    try:
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')
            
        for eachLine in splitSource:
            splitLine = eachLine.split(',')
            if len(splitLine) == 6:
                if 'values' not in eachLine:
                    
                    v1 = datetime.datetime.strptime(splitLine[0], '%Y%m%d').strftime('%Y, %m, %d')
                    v2 = splitLine[1]
                    v3 = splitLine[2]
                    v4 = splitLine[3]
                    v5= splitLine[4]
                    v6 = splitLine[5]
                   
                    cursor.execute('INSERT INTO stock_historic_data(stock_tickers,price_date,price_close,price_high,price_low ,price_open,volume)' \
                              ' VALUES(%s,%s,%s,%s,%s,%s,%s)',(stock,v1,v2,v3,v4,v5,v6))

        print 'Pulled '+ stock
        print 'sleeping'
        time.sleep(5)
        mydb.commit()
        cursor.close()
        print "Done"
        
    except Exception ,e:
        print 'main loop',str(e)


pullData(stocks)


