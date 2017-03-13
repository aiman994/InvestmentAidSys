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

def getSectorList():

            sectorList=[]
            response = urllib.urlopen('https://biz.yahoo.com/p/csv/s_conameu.csv')
            csvfile = csv.reader(x.replace('\0',"") for x in response) ## change blank row into string
            intoList=map(tuple,csvfile)
            i=0

            for eachrow in intoList:
                splitline = eachrow
                if eachrow:# check if row empty
                    if 'Sectors' not in eachrow:
                     
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

            mydb.commit()
            cursor.close()     

def getIndustryListbysectors():
    
      # for sector in range(1,9):
          
            url="https://biz.yahoo.com/p/1conameu.html"
            htmlfile= urllib.urlopen(url).read()

            industryList=[]
            urlindustry=[]
            data=[]
            #html parser

            parser= soup(htmlfile,"lxml")

            tables = parser.find("table", {"bgcolor":"dcdcdc"})

            for row in tables:
                cells = row.findAll("td", {"bgcolor":"ffffee"}) # carik column name of industry
                cell2 = row.findAll("td", {"align":"right"})

            for x in range(0,len(cells)):#setiap column
                industryList.append(cells[x].find('font', {'face':"arial"}).text)
                if cells[x].a:
                    urlindustry.append(cells[x].a.get('href')) # got the url of the industry

            
            for y in range(0,len(cell2)): 
                if y < 9:
                    data.append(cell2[y].find('font', {'face':"arial"}).text)


            #url = urlindustry[0]
            company = getcompanyList(urlindustry[0])
            print "DATA FOR INDUSTRY 1"+data[1]





def getcompanyList(urlindustry):
        #for i in range (0):
            urltoopen= "https://biz.yahoo.com/p/"+urlindustry

            htmlfile= urllib.urlopen(urltoopen).read()
        
            companyList=[]
            tickerList=[]
            #html parser

            parser= soup(htmlfile,"lxml")

            tables = parser.find("table", {"bgcolor":"dcdcdc"})

            for row in tables:
                    cells = row.findAll("td", {"bgcolor":"ffffee"}) # carik column skali


            for x in range(0,len(cells)):#setiap column 
                    companyList.append(cells[x].a.text)
                    nextSib=cells[x].a.next_sibling
                    
            for t in parser.findAll(text=' ('):
                        print t.nextSibling.string
##                        for item in t.parent.next_siblings:
##                            print t.parent.next_siblings
##                            if isinstance(item, Tag):
##                                if 'class' in item.attrs and 'name' in item.attrs['class']:
##                                    break
##                                print t
                    
                    #tickerList.append(nextSib.text())
                            #urlindustry.append(cells[x].a.get('href'))
            
            print "COMPANY \n\n"
            #print cells


def getIndustryList():
               urltoopen= "https://biz.yahoo.com/p/sum_conameu.html"

               htmlfile= urllib.urlopen(urltoopen).read()

               industryList=[]
               urlindustry=[]
               companyList=[]
               #html parser

               parser= soup(htmlfile,"lxml")

               tables = parser.find("table", {"bgcolor":"dcdcdc"})

               for row in tables:
                     cells = row.findAll("td", {"bgcolor":"ffffee"}) # carik column skali


               for x in range(0,len(cells)):#setiap rows and column 
                     industryList.append(cells[x].a.text)
                     urlindustry.append(cells[x].a.get('href'))


               #url = urlindustry[0]
               #company = getcompanyList(urlindustry)
               print industryList

getIndustryListbysectors()
