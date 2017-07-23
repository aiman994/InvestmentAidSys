import lxml.html as LH
import requests
import pandas as pd
import MySQLdb
import datetime 
import re
from textblob import TextBlob
import sys
ticker= sys.argv[1]

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='1234',
    db='investmentaidsys')

cursor = mydb.cursor()
############################################################################
def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')
###########################################################################

r = requests.get("http://finance.yahoo.com/quote/%s?p=%s"%(ticker,ticker))
root = LH.fromstring(r.content)

lists=[]

for summ in root.xpath('//div[contains(@data-test,"summary-table")]//tr'):
    
    left=[th for th in summ.xpath('//div[contains(@data-test,"left-summary-table")]')]
    
for each in left:
    apa = each.xpath('//table/tbody/tr/td')
    for each in apa:
        if 'Search' not in text(each):
            if 'Previous Close' not in text(each):
                if 'Open' not in text(each):
                    if 'Bid' not in text(each):
                        if 'Ask' not in text(each):
                            if "Day's Range" not in text(each):
                                if '52 Week Range' not in text(each):
                                    if 'Volume' not in text(each):
                                        if 'Avg. Volume' not in text(each):
                                            if 'Market Cap' not in text(each):
                                                if 'Beta' not in text(each):
                                                    if 'PE Ratio (TTM)' not in text(each):
                                                        if 'EPS (TTM)' not in text(each):
                                                            if 'Earnings Date' not in text(each):
                                                                if 'Dividend & Yield' not in text(each):
                                                                    if 'Ex-Dividend Date' not in text(each):
                                                                        if '1y Target Est' not in text(each):
                                                                            lists.append(text(each))

#####################################
cursor.execute("SELECT stock_tickers FROM company_summaries WHERE stock_tickers = %s" , [ticker])
msg = cursor.rowcount
if msg==0:
    v1=lists[1]
    v2=lists[2]
    v3=lists[3]
    v4=lists[4]
    v5=lists[5]
    v6=lists[6]
    v7=lists[7]
    v8=lists[8]
    v9=lists[9]
    v10=lists[10]
    v11=lists[11]
    v12=lists[12]
    v13=lists[13]
    v14=lists[14]
    v15=lists[15]
    v16=lists[16]
    now = datetime.datetime.now()
    cursor.execute('INSERT INTO company_summaries(stock_tickers,prevClose,open,bid,ask,dayRange,fiftytwoWRange,volume,avgvol,marketCap,Beta,PEratioTTM,EPSttm,earningDate,DividentYield,ExdivDate,yearTargetEst,created_at,updated_at)' \
                              ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(ticker, v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,now,now))

    mydb.commit()
elif msg>0:
    v1=lists[1]
    v2=lists[2]
    v3=lists[3]
    v4=lists[4]
    v5=lists[5]
    v6=lists[6]
    v7=lists[7]
    v8=lists[8]
    v9=lists[9]
    v10=lists[10]
    v11=lists[11]
    v12=lists[12]
    v13=lists[13]
    v14=lists[14]
    v15=lists[15]
    v16=lists[16]
    now = datetime.datetime.now()
    cursor.execute("UPDATE company_summaries " \
        "SET prevClose='"+v1+"', open='"+v2+"', bid='"+v3+"', ask='"+v4+"', dayRange='"+v5+"',fiftytwoWRange='"+v6+"'" \
        ",volume='"+v7+"',avgvol='"+v8+"',marketCap='"+v9+"',Beta='"+v10+"',PEratioTTM='"+v11+"',EPSttm='"+v12+"'" \
        " ,earningDate='"+v13+"',DividentYield='"+v14+"',ExdivDate='"+v15+"',yearTargetEst='"+v16+"',created_at='"+str(now)+"',updated_at='"+str(now)+"' WHERE stock_tickers= %s" , [ticker] )
    mydb.commit()
    cursor.close()


cursor.close()
