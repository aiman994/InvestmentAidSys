from facepy import GraphAPI
import MySQLdb
import sys
import datetime
from textblob import TextBlob
stocks = sys.argv[1]


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

graph = GraphAPI('EAACEdEose0cBAJnel1h6iV2fV2AIrQ9c8knEemYX77RDBH2T4pPzJYgp7pRYDR9iP4bj8cpeTZBxiPZCYLOZBLZAZCaJ6XJmZAybO5ZBElN8nUaAXtQ1ZCSLMtRqZBqRijFvrGEwVXq8I4VD6fViQQFW2CYZBHNOekgSGlIODRzCEChG3FJ4z4ziJ0f6pjUdTjq30ZD')
listpages= ["cnninternational" , "bloombergbusiness"]
wordList=[]

cursor.execute ("select company_name,stock_tickers from company where stock_tickers='"+stocks+"'")
data= cursor.fetchall()
for each in data:
    Compname= each[0]
print " got company name "+ Compname


breaks= TextBlob(Compname)
for each in breaks.words:
    wordList.append(each)
    

for each in listpages:
    count=0
    # Get my latest posts
    pages = graph.get(each+'/posts?fields=message,created_time,picture,permalink_url', page=True)
    for page in pages:
        if count <=20:
            count+=1
            for post in page["data"]:
                if "message" in post:
                    if wordList[0] in post["message"]:
                       now = datetime.datetime.now() 
                       v1 = post["message"]
                       v2 = post["created_time"]
                       v3 = post["picture"]
                       v4 = post["permalink_url"]

                       cursor.execute("SELECT stock_name,posts_url FROM fb_streams WHERE stock_name= '"+stocks+"' AND posts_url='"+v4+"'")
                       msg1 = cursor.fetchall()
                       if len(msg1)>=1:
                           print "already saved earlier"
                       elif len(msg1)<1:
                           synopsis = TextBlob(post["message"])
                           polar=(synopsis.sentiment.polarity)
                           subject=(synopsis.sentiment.subjectivity)
                           cursor.execute('INSERT INTO fb_streams(stock_name,fb_user,post,pic_url,posts_url,time_posted,created_at,updated_at,polarity,subjectivity)' \
                                              ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(stocks,each,v1,v3,v4,v2,now,now,polar,subject))
                           mydb.commit()
        elif count>20:
          print " no new fb posts"
          break

    break
cursor.close()





