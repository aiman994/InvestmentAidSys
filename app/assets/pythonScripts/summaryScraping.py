from lxml import html  
import requests
from exceptions import ValueError
import json
from collections import OrderedDict
import datetime
import MySQLdb
import sys
stocks = sys.argv[1]

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='1234',
    db='investmentaidsys')

cursor = mydb.cursor()


def parse(ticker):
        url = "http://finance.yahoo.com/quote/%s?p=%s"%(ticker,ticker)
        response = requests.get(url)
        print "Parsing %s"%(url)
        parser = html.fromstring(response.text)
        summary_table = parser.xpath('//div[contains(@data-test,"summary-table")]//tr')
        summary_data = OrderedDict()
        other_details_json_link = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{0}?formatted=true&lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents&corsDomain=finance.yahoo.com".format(ticker)
        summary_json_response = requests.get(other_details_json_link)
        try:
                json_loaded_summary =  json.loads(summary_json_response.text)
                y_Target_Est = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["targetMeanPrice"]['raw']
                earnings_list = json_loaded_summary["quoteSummary"]["result"][0]["calendarEvents"]['earnings']
                eps = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["trailingEps"]['raw']
                datelist = []
                for i in earnings_list['earningsDate']:
                        datelist.append(i['fmt'])
                earnings_date = ' to '.join(datelist)
                for table_data in summary_table:
                        raw_table_key = table_data.xpath('.//td[@class="C(black)"]//text()')
                        raw_table_value = table_data.xpath('.//td[contains(@class,"Ta(end)")]//text()')
                        table_key = ''.join(raw_table_key).strip()
                        table_value = ''.join(raw_table_value).strip()
                        summary_data.update({table_key:table_value})
                summary_data.update({'1y Target Est':y_Target_Est,'EPS (TTM)':eps,'Earnings Date':earnings_date,'ticker':ticker,'url':url})
                print summary_data
                return summary_data
    
        except ValueError:
                print "Failed to parse json response"
                return {"error":"Failed to parse json response"}
                

print "Fetching data for %s"%(stocks)
x=0
cursor.execute("SELECT stock_tickers FROM company_summaries WHERE stock_tickers = %s" , [stocks])
msg = cursor.rowcount
print msg
if msg==0:
    scraped_data = parse(stocks)
    print scraped_data
    v1=scraped_data.items()[0][1]
    v2=scraped_data.items()[1][1]
    v3=scraped_data.items()[2][1]
    v4=scraped_data.items()[3][1]
    v5=scraped_data.items()[4][1]
    v6=scraped_data.items()[5][1]
    v7=scraped_data.items()[6][1]
    v8=scraped_data.items()[7][1]
    v9=scraped_data.items()[8][1]
    v10=scraped_data.items()[9][1]
    v11=scraped_data.items()[10][1]
    v12=scraped_data.items()[11][1]
    v13=scraped_data.items()[12][1]
    v14=scraped_data.items()[13][1]
    v15=scraped_data.items()[14][1]
    v16=scraped_data.items()[15][1]
    now = datetime.datetime.now()
    cursor.execute('INSERT INTO company_summaries(stock_tickers,prevClose,open,bid,ask,dayRange,fiftytwoWRange,volume,avgvol,marketCap,Beta,PEratioTTM,EPSttm,earningDate,DividentYield,ExdivDate,yearTargetEst,created_at,updated_at)' \
                              ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(stocks, v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,now,now))

    mydb.commit()
elif msg>0:
    print "dah ada"
    scraped_data = parse(stocks)
    print scraped_data
    v1=scraped_data.items()[0][1]
    v2=scraped_data.items()[1][1]
    v3=scraped_data.items()[2][1]
    v4=scraped_data.items()[3][1]
    v5=scraped_data.items()[4][1]
    v6=scraped_data.items()[5][1]
    v7=scraped_data.items()[6][1]
    v8=scraped_data.items()[7][1]
    v9=scraped_data.items()[8][1]
    v10=scraped_data.items()[9][1]
    v11=scraped_data.items()[10][1]
    v12=scraped_data.items()[11][1]
    v13=scraped_data.items()[12][1]
    v14=scraped_data.items()[13][1]
    v15=scraped_data.items()[14][1]
    v16=scraped_data.items()[15][1]
    now = datetime.datetime.now()
    cursor.execute("UPDATE prediction_data " \
        "SET prevClose='"+v1+"', open='"+v2+"', bid='"+v3+"', ask='"+v4+"', dayRange='"+v5+"',fiftytwoWRange='"+v6+"'" \
        ",vol='"+v7+"',avgvol='"+v8+"',marketCap='"+v9+"',Beta='"+v10+"',PEratioTTM='"+v11+"',EPSttm='"+v12+"'" \
        "earningDate='"+v13+"',DividentTield='"+v14+"',ExdivDate+'"+v15+"',yearTargetEst='"+v16+"',created_at='"+now+"',updated_at='"+now+"'" \
        "WHERE stock_tickers='"+stocks+ "' AND created_at='"+dates+"'" )
    mydb.commit()
    cursor.close()

cursor.close()
    

    



