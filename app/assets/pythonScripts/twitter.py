from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import MySQLdb
import sys
import datetime
stock=sys.argv[1] 

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='1234',
    db='investmentaidsys')
cursor = mydb.cursor()

mydb.set_character_set('utf8mb4')
cursor.execute('SET NAMES utf8mb4;')
mydb.commit()
cursor.execute('SET CHARACTER SET utf8mb4;')
mydb.commit()
cursor.execute('SET character_set_connection=utf8mb4;')
mydb.commit()
 
#consumer key, consumer secret, access token, access secret.
ckey="MvtrEOkP6L1zzCEKFHiBBiFAL"
csecret="oAreNlEHaOzSkqCplqezlL4FnINtGRHv8a7wdzB3hrkYHURobj"
atoken="859216909-jpy6SKs1SB2VzxcIGx4UCWs8L4D2jeP8rloth2m8"
asecret="H3dhGUc9LADNBkhdHwFPmjKcTMGYZSb0jJoZh82evnwZa"
class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        picUrl=all_data["user"]["profile_image_url_https"]
        date=all_data["created_at"]
        now = datetime.datetime.now()
        cursor.execute('INSERT INTO twitter_streams(stock_name,username,tweets,profile_pic_url,created_at,updated_at)' \
                          ' VALUES(%s,%s,%s,%s,%s,%s)',(stock,username,tweet,picUrl,date,now))
        mydb.commit()
        print date + "\n"
        return True


    def on_error(self, status):
        print status
        cursor.close()

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["$"+stock], async=True)
