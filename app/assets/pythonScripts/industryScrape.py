import urllib                           ## use to open url
from bs4 import BeautifulSoup as soup   ## use to parse the html
import csv                              ## use to read the csv file
import MySQLdb                          ## to insert into db


mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='investmentaidsys')

cursor = mydb.cursor()
## database connection

def getcompanyList(urlindustry):
     
    #for i in range(0,len(urlindustry)):
          industryUrl= "https://biz.yahoo.com/p/"+urlindustry[0]
          companyhtml= urllib.urlopen(industryUrl).read()
          parser2 = soup(companyhtml,"html5lib")
          return rows


def getIndustryList():
	urltoopen= "https://biz.yahoo.com/p/sum_conameu.html"

	htmlfile= urllib.urlopen(urltoopen).read()

	industryList=[]
	urlindustry=[]
	companyList=[]
	#html parser

	parser= soup(htmlfile,"html5lib")

	tables = parser.find("table", {"bgcolor":"dcdcdc"})

	for row in tables:
	    cells = row.findAll("td", {"bgcolor":"ffffee"}) # carik column skali


	for x in range(0,len(cells)):#setiap rows and column 
	    industryList.append(cells[x].a.text)
	    urlindustry.append(cells[x].a.get('href'))


	url = urlindustry[0]
	company = getcompanyList(urlindustry)
	#print company

def getSectorList():

    sectorList=[]
    response = urllib.urlopen('https://biz.yahoo.com/p/csv/s_conameu.csv')
    csvfile = csv.reader(x.replace('\0',"") for x in response) ## change blank row into string
    intoList=map(tuple,csvfile)
    i=0

    for eachrow in intoList:
        splitline = eachrow
        if eachrow:
            if 'Sectors' not in eachrow:
             # check if row empty
              #  sectorList.append(splitline[0])
                v1=splitline[0]
                v2=splitline[1]
                v3=splitline[2]  
                v4=splitline[3]  
                v5=splitline[4]
                v6=splitline[5]
                v7=splitline[6]
                v8=splitline[7]
                v9=splitline[8]
                v10=splitline[9] 
                cursor.execute('INSERT INTO stock_sectors(sectors_name,dayprice_change,market_cap,p_earning,returnEquity,div_yield,longTermDebttoEquity,priceTobook,netProfitMargin,priceToFreecashFlow)' \
                              ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10))
                
                print 'insert into db'
         
        #else:
         #   pass # kalau empty list skip



    cursor.close()     



getSectorList()
