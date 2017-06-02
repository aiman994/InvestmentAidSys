from facepy import GraphAPI
import MySQLdb
import sys
import datetime

stocks = "Apple" #sys.argv[1]

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='investmentaidsys')
cursor = mydb.cursor()

# Initialize the Graph API with a valid access token (optional,
# but will allow you to do all sorts of fun stuff).
graph = GraphAPI('EAACEdEose0cBAK6Q4Hv2pAtMxfl4InSAHDS4I6wZCUy0krsUJNk2upidUKPJk1ghED2Gs4aTnbJ2Pve3plMyxpPVBabLjHlJzWTZChmLm4wOE589fzDwPvwXSLZCA1gUM4Ah6tKQZCXEBeStaxWRP2hHZCoiAZB6SJLWN6ehOZBf69yZBZAeMakqNORXGH8g9160ZD')
listpages= ["cnninternational"]
for each in listpages:
    # Get my latest posts
    pages = graph.get(each+'/posts?fields=message,created_time,picture,permalink_url', page=True)
    for page in pages:
        for post in page["data"]:
            if "message" in post:
                if stocks in post["message"]:
                   now = datetime.datetime.now() 
                   v1 = post["message"]
                   v2 = post["created_time"]
                   v3 = post["picture"]
                   v4 = post["permalink_url"]
                   cursor.execute('INSERT INTO fb_streams(stock_name,fb_user,post,pic_url,posts_url,time_posted,created_at,updated_at)' \
                              ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(stocks,each,v1,v3,v4,v2,now,now))
                   mydb.commit()
                   print post["created_time"]

    
cursor.close()

#"



