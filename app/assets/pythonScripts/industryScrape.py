import urllib                           ## use to open url
from bs4 import BeautifulSoup as soup   ## use to parse the html
import csv                              ## use to read the csv file
import MySQLdb                          ## to insert into db
import datetime

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='investmentaidsys')
    
cursor = mydb.cursor()

mydb.set_character_set('utf8mb4')
cursor.execute('SET NAMES utf8mb4;')
mydb.commit()
cursor.execute('SET CHARACTER SET utf8mb4;')
mydb.commit()
cursor.execute('SET character_set_connection=utf8mb4;')
mydb.commit()
## database connection##########################################################

def getSectorList():

            sectorList=[]
            response = urllib.urlopen('https://biz.yahoo.com/p/csv/s_conameu.csv')
            csvfile = csv.reader(x.replace('\0',"") for x in response) ## change blank row into string
            intoList=map(tuple,csvfile)
            

            for eachrow in intoList:
                splitline = eachrow
                if eachrow:# check if row empty
                    if 'Sectors' not in eachrow:
                         

                        now = datetime.datetime.now()
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
            
#############################################################################################################################

def getIndustryListbysectors():
      cursor.execute('TRUNCATE TABLE stock_industry;')
      mydb.commit()
      cursor.execute('TRUNCATE TABLE companies;')
      mydb.commit()
      
      for sector in range(1,10):
            count=1  
            url="https://biz.yahoo.com/p/"+str(sector)+"conameu.html"
            htmlfile= urllib.urlopen(url).read()
            
            industryList=[] #setiap kali loop buat list baru 
            urlindustry=[]          
            data=[]
            databasedrows=[]
            sectorr=[]
            industry=[]
            
            parser= soup(htmlfile,"lxml") ########html parser
            tables = parser.find("table", {"bgcolor":"dcdcdc"})

            for row in tables:
                cells = row.findAll("td", {"bgcolor":"ffffee"}) # carik column name of industry
                celldata = row.findAll("td", {"align":"right"})

            for x in range(0,len(cells)):#setiap column
                industryList.append(cells[x].find('font', {'face':"arial"}).text.replace("\n", ' ')) #got the industry name
                if cells[x].a:
                    urlindustry.append(cells[x].a.get('href'))                  # got the url of the company

            for y in range(9,len(celldata)):
                    data.append(celldata[y].find('font', {'face':"arial"}).text)


            databasedrows=list(chunks(data, 9)) # data based on row
            i=0
            for eachrow in databasedrows:
                
                splitline = eachrow
                sectors=industryList[0].split(': ')
                sectorr=sectors[1]
                industry=industryList[count]
                url= urlindustry[i]
                print industry
                if eachrow: # check if row empty
                        now = datetime.datetime.now()
                        v1=splitline[0]
                        v2=splitline[1]
                        v3=splitline[2]  
                        v4=splitline[3]  
                        v5=splitline[4]
                        v6=splitline[5]
                        v7=splitline[6]
                        v8=splitline[7]
                        v9=splitline[8] 
                        cursor.execute('INSERT INTO stock_industry(industry_name,industry_sector,dayprice_change,market_cap,p_earning,returnEquity,div_yield,longTermDebttoEquity,priceTobook,netProfitMargin,priceToFreecashFlow,updated_at)' \
                                      ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(industry, sectorr,v1,v2,v3,v4,v5,v6,v7,v8,v9,now))
                        count+=1
                        mydb.commit()
                        i+=1
                        print i
                        
                if i < count:
                        getcompanyList(url,sectorr,industry)    

                    
                
                    
            

      cursor.close()
           
#################################################################################################################
            

def chunks(l, n): # to cut the data into rows
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

#################################################################################################################

def getcompanyList(url,sector,industry):
        
    
##        for i in range (0,len(urlindustry)):
            countticker=0
            companyList=[]
            tickerList=[]
            count = 0
            combo=[]
            nourl=0
            urltoopen= "https://biz.yahoo.com/p/"+url
            htmlfile= urllib.urlopen(urltoopen).read()
            #html parser

            parser= soup(htmlfile,"lxml")
            tables = parser.find("table", {"bgcolor":"dcdcdc"})

            for row in tables:
                    cells = row.findAll("td", {"bgcolor":"ffffee"}) # carik column skali

            
            for x in range(2,len(cells)):   #setiap column
                        companyList.append(cells[x].a.text.replace("\n", ' '))
                        nextSib = cells[x].a.nextSibling
                        strings= str(nextSib)
                        if len(strings) != 4:
                            combo.append(strings)
            
            withUrl=parser.findAll(text=' (')
            witN = parser.findAll(text='\n(')

            for t in range(0,len(combo)):
                        
                        if len(combo[t])<5:
                           total= t-count
                           total2=t-nourl+1
                           if '\n(' not in combo[t]:
                               if total < len(withUrl):
                               
                                   value=withUrl[total].nextSibling.text
                                   tickerList.append(value)
                                   nourl+=1
                                   
                           elif '\n(' in combo[t]:
                                   value=witN[total2].nextSibling.text

                                   tickerList.append(value)
                                   count+=1
                                       
                               
                        else:
                            tickerList.append(combo[t].replace("\n", ' '))
                            nourl+=1
                            count+=1

            for eachrow in companyList:
                company = eachrow
                
                if eachrow: # check if row empty
                        now = datetime.datetime.now()
                        cursor.execute('INSERT INTO company(company_name,stock_tickers,company_sector,company_industry,updated_at)' \
                                      ' VALUES(%s,%s,%s,%s,%s)',(company,tickerList[countticker],sector, industry, now))
                        
                countticker+=1
                
            mydb.commit()
            print industry +" companies done into db"
####################################################################################################################################################
            


getIndustryListbysectors()
