import pandas_datareader.data as web
import datetime
import time
import sys
import MySQLdb
import pandas as pd
stocks = "AAPL"#sys.argv[1]

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='investmentaidsys')

cursor = mydb.cursor()

#************************************************************************************************888
# FIND EXCHANGE FIRST
cursor.execute ("select stock_tickers,exchange from company where stock_tickers='"+stocks+"'")
data= cursor.fetchall()
for each in data:
    exchange= each[1]
##############################################
end = datetime.datetime.now() # ** is the current date. new date
start = datetime.datetime(2014,end.month,end.day)# past date
stockexchange= exchange+":"+stocks
print start

try:
    cursor.execute("SELECT stock_tickers FROM stock_historic_data WHERE stock_tickers = %s" , [stocks])
    msg = cursor.rowcount
    currentTimePosix = int(round((time.mktime(end.timetuple()))*1000))
    #if xda dalam DB
    if msg == 0:
          print 'Pulling data... google '+ stocks
          # pull from google using API,  convert date into posix ,insert into Db
          df1=web.DataReader(stockexchange, 'google', start, end)
          for index,row in df1.iterrows():
              dates = time.mktime(datetime.datetime.strptime(str(index), "%Y-%m-%d %H:%M:%S").timetuple())
              pdate= int(round(dates*1000))
              pclose= str(row['Close'])
              popen= str(row['Open'])
              phigh= str(row['High'])
              plow= str(row['Low'])
              pvol= str(row['Volume'])

              cursor.execute('INSERT INTO stock_historic_data(stock_tickers,price_date,price_close,price_high,price_low ,price_open,volume,created_at,updated_at)' \
                              ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(stocks, pdate,pclose,phigh,plow,popen,pvol,end,end))

        
    elif msg > 0:
        cursor.execute("SELECT stock_tickers,MAX(price_date) FROM stock_historic_data WHERE stock_tickers= '"+stocks+"'")
        msg1 = cursor.fetchall()
        if len(msg1)>0:
            print " dah adaa \n"
            for each in msg1:
                print msg1
                date=int(each[1])/1000
                date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date))
                latestDate = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                print latestDate
                if latestDate.date() == (datetime.datetime.now()-datetime.timedelta(days=1)).date():
                    print latestDate
                    print " up to date"
                else:
                    print " db"
                    strt= latestDate+ datetime.timedelta(days=1)
                    ends = datetime.datetime.now()
                    df1=web.DataReader(stockexchange, 'google', strt, ends)
                    
                    for index,row in df1.iterrows():
                        dates = time.mktime(datetime.datetime.strptime(str(index), "%Y-%m-%d %H:%M:%S").timetuple())
                        pdate= int(round(dates*1000))
                        pclose= str(row['Close'])
                        popen= str(row['Open'])
                        phigh= str(row['High'])
                        plow= str(row['Low'])
                        pvol= str(row['Volume'])

                        cursor.execute('INSERT INTO stock_historic_data(stock_tickers,price_date,price_close,price_high,price_low ,price_open,volume,created_at,updated_at)' \
                                      ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(stocks, pdate,pclose,phigh,plow,popen,pvol,ends,ends))
        else:
            print " no data with tickers" + stocks
                    
            
    mydb.commit()  
except Exception, e:
    print str(e)
      

cursor.close()
