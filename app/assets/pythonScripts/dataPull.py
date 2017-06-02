import pandas_datareader.data as web
import datetime
import time
import sys
import MySQLdb
import pandas as pd
stocks = sys.argv[1]

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='investmentaidsys')

cursor = mydb.cursor()

#************************************************************************************************888

end = datetime.datetime.now() # ** is the current date. new date
start = datetime.datetime(2014,end.month,end.day)#past date



# check db ada data ticker tu ke x
try:
    cursor.execute("SELECT stock_tickers FROM stock_historic_data WHERE stock_tickers = %s" , [stocks])

    msg = cursor.rowcount
    currentTimePosix = int(round((time.mktime(end.timetuple()))*1000))
    #if xda
    if msg == 0:
          print 'Pulling data... google '+ stocks
          # pull from google using API,  convert date into posix ,insert into Db
          df1=web.DataReader(stocks, 'google', start, end)
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

  
    mydb.commit()          
                
 '''   if msg !=0:
        cursor.execute("SELECT stock_tickers,price_date FROM stock_historic_data WHERE stock_tickers= %s AND price_date= %s" , [[stocks, currentTimePosix]])
        msg1 = cursor.rowcount
        #if yes
                #no need to pull 
        # if not
        if msg1 != 0:
          print "dah pull"
 #            cursor.execute('INSERT INTO stock_historic_data(stock_tickers,price_date,price_close,price_high,price_low ,price_open,volume,updated_at)' \
        
  #                            ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(stock,v1,v2,v3,v4,v5,v6,now))'''

except Exception, e:
    print str(e)
      

cursor.close()