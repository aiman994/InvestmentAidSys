import lxml.html as LH
import requests
import pandas as pd
import MySQLdb
import datetime 
import re
from textblob import TextBlob
import sys
companynme= sys.argv[1]

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
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
##companynme= "samsung"
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


print "pulling data from...." + CompanyintoWord(companynme)
r = requests.get(CompanyintoWord(companynme))
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
    
    synopsis = TextBlob(content)
    polarList.append(synopsis.sentiment.polarity)
    subjectList.append(synopsis.sentiment.subjectivity)
    storyList.append(content)

for each in title:
    titles= str(each).replace(' u" ', "")
    titles = titles.replace(" u' ", "")
    titleList.append(titles)
    
for each in dates:
    zen= each.split("', u' ")
    date= str(zen).replace("u'","")
    dateList.append(date)

    
df = pd.DataFrame(columns=['headline', 'story', 'URL'])
if len(storyList)== len(newsUrl) & len(storyList) == len(titleList):
    x=0
    while x < len(newsUrl):
        now = datetime.datetime.now()
        cursor.execute('INSERT INTO bloomberg_streams(companyNme,newsDate,headlines,story,newsUrl,polarity,subjectivity,created_at,updated_at)' \
                              ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(companynme,dateList[x],titleList[x],storyList[x],newsUrl[x],polarList[x],subjectList[x],now,now))
        x+=1
        print x
   
mydb.commit()
cursor.close()
