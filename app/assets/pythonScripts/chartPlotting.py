<<<<<<< HEAD
import MySQLdb
import sys
import json

stocks = sys.argv[1]
DataArr =[]

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='investmentaidsys')
cursor = mydb.cursor()
cursor2= mydb.cursor()

def pullDbData(stock):

        try:
            fileLine = 'app/assets/'+stock+'.txt'
            try:
                    
                   cursor.execute('SELECT * FROM stock_historic_data    WHERE stock_tickers = %s ',(stock)) #WHERE stock_tickers = %s',(stock))
                   rows= cursor.fetchone()
                   
                   while rows is not None:
                          # print 'ooolaa'
                           DataArr.append(rows)
                           rows= cursor.fetchone()
                           

                
            except Exception ,e:
                    print 'main loop',str(e)
        
          # print DataArr[101]
            saveFile = open(fileLine,'a')
          
            for each in DataArr:
                    lineToWrite = each
                    saveFile.write(json.dumps(each))

        mydb.commit()
        cursor.close()
        print json.dumps(DataArr)
        except Exception ,e:
            print 'main loop',str(e)



pullDbData(stocks)
=======
import MySQLdb
import sys
import json

stocks = sys.argv[1]
DataArr =[]

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='investmentaidsys')
cursor = mydb.cursor()
cursor2= mydb.cursor()

def pullDbData(stock):

        try:
            fileLine = 'app/assets/'+stock+'.txt'
            try:
                    
                   cursor.execute('SELECT * FROM stock_historic_data    WHERE stock_tickers = %s ',(stock)) #WHERE stock_tickers = %s',(stock))
                   rows= cursor.fetchone()
                   
                   while rows is not None:
                          # print 'ooolaa'
                           DataArr.append(rows)
                           rows= cursor.fetchone()
                           

                
            except Exception ,e:
                    print 'main loop',str(e)
        
          # print DataArr[101]
            saveFile = open(fileLine,'a')
          
            for each in DataArr:
                    lineToWrite = each
                    saveFile.write(json.dumps(each))

        mydb.commit()
        cursor.close()
        print json.dumps(DataArr)
        except Exception ,e:
            print 'main loop',str(e)



pullDbData(stocks)
>>>>>>> b5b8d16e79fff0e954da458cad9af177739ebb67
