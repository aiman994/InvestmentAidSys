import lxml.html as LH
import requests
import pandas as pd
import MySQLdb
import datetime 
import re
from textblob import TextBlob
import sys
stocks= sys.argv[1]

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='1234',
    db='investmentaidsys')

cursor = mydb.cursor()
################################################################################
dateList=[]
wordList=[]
newsUrl=[]
titleList=[]
storyList=[]
polarList=[]
subjectList=[]

story=""
title=""
dates=""


#####################################################################################
def text(elt):
    return elt.text_content().replace(u'\xa0', u' ')

############################################################################ break down company name into words

def CompanyintoWord(comp):
    url = 'https://www.bloomberg.com/search?query='
    breaks= TextBlob(comp)
    for each in breaks.words:
        wordList.append(each)

    numofwords=len(wordList)
    for i in range(numofwords):
        if i+1 != numofwords:
            url+=wordList[i]+"+"
        elif i+1== numofwords:
            url+=wordList[i]
    return url

cursor.execute ("select company_name,stock_tickers from company where stock_tickers='"+stocks+"'")
data= cursor.fetchall()
for each in data:
    Compname= each[0]

print "pulling data from bloomberg for...." + CompanyintoWord(Compname)

r = requests.get(CompanyintoWord(Compname))
root = LH.fromstring(r.content)



for news in root.xpath('//div[@class="container"]'):
    
    title=[text(th) for th in news.xpath('//main/div/section/section/section/div/div/article/div/h1[@class="search-result-story__headline"]')]
    story=[text(th) for th in news.xpath('//main/div/section/section/section/div/div/article/div/div[@class="search-result-story__body"]')]
    dates=[text(th) for th in news.xpath('//main/div/section/section/section/div/div/article/div/div/span/time[@class="published-at"]')]

    
    for links in news.xpath('//main/div/section/section/section/div/div/article/div/h1//a/@href'):
         newsUrl.append(links)
         
for each in story:
    zen= each.split("... ', ")
    content= str(zen).replace("\\u201c","")
    content= content.replace("\\u2019","")
    content= content.replace("u' ","")
    content= content.replace("      ","")
    content= content.replace('u" ',"")
    content= content.replace("[","")
    content= content.replace("']","")
    synopsis = TextBlob(content)
    polarList.append(synopsis.sentiment.polarity)
    subjectList.append(synopsis.sentiment.subjectivity)
    storyList.append(content)
    
for each in title:

    titles= each.encode('utf-8').strip().replace(' u" ', "")
    titles = titles.replace(" u' ", "")
    titleList.append(titles)
    
for each in dates:
    zen= each.split("', u' ")
    date= str(zen).replace("u'","")
    date= date.replace("[","")
    date= date.replace("']","")
    dateList.append(date)

if len(storyList)== len(newsUrl) & len(storyList) == len(titleList):
    for each in newsUrl:
        cursor.execute("SELECT companyNme,newsUrl FROM bloomberg_streams WHERE companyNme= '"+ stocks +"' AND newsUrl='"+each+"'")
        msg1 = cursor.fetchall()
        print msg1
        if  len(msg1)<1:
            x=0
            while x < len(newsUrl):
                now = datetime.datetime.now()
                cursor.execute('INSERT INTO bloomberg_streams(companyNme,newsDate,headlines,story,newsUrl,polarity,subjectivity,created_at,updated_at)' \
                                      ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(stocks,dateList[x],titleList[x],storyList[x],newsUrl[x],polarList[x],subjectList[x],now,now))
                x+=1
        elif len(msg1)>=1:
            print "already saved earlier"

mydb.commit()
cursor.close()
