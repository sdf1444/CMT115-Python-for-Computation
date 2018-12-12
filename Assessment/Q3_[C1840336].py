import sys
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from textblob import TextBlob
import sqlite3

#Pass security information to variables.
#Code adapted from tweepy documentation.
#Accessed 16/11/18.
#http://docs.tweepy.org/en/v3.5.0/index.html.
consumer_key = 'QAqwPzNLEODn0lJQSdDjcr43m'
consumer_secret = 't0IPOhjUxxQtxEdEsBRHctbztSC4P2iKpAL8on1a5KY6CbKxpk'
access_token = '22181511-aYQOnMO6bsGeP5bLl8P81yRSPG7cJ4njAT19snisc'
access_secret = 'EOt8LJX12kDW8AcZnR4oTLtQ3Cxk2eiz1pzWwvv2yXsof'
#End of reference.

#Connect to sqlite and create a Trump tweet data table.
#Code adapted from stackoverflow.
#Accessed 02/12/18.
#https://stackoverflow.com/questions/24502512/python-how-do-i-write-an-infinite-stream-to-a-sqlite-database-and-perform-query
conn = sqlite3.connect('Q3_sqlite_[C1840336].db')
c = conn.cursor()
c.execute('''CREATE TABLE Trump(ID, Tweet, Created_at, Location, Geo_coordinates, Followers_for_the_user, Friends, Sentiment_analysis)''')
#End of reference.

#Use variables to access twitter.
#Code adapted from tweepy documentation.
#Accessed 16/11/18.
#http://docs.tweepy.org/en/v3.5.0/auth_tutorial.html#oauth-authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
#End of reference.

#Streaming with Tweepy.
#Code adapted from tweepy documentation.
#Accessed 16/11/18.
#http://docs.tweepy.org/en/v3.5.0/streaming_how_to.html
class MyListener(StreamListener):
 
    def on_status(self, status):
        analysis = TextBlob(status.text)
        c.execute("INSERT INTO Trump (ID, Tweet, Created_at, Location, Geo_coordinates, Followers_for_the_user, Friends, Sentiment_analysis) VALUES(?,?,?,?,?,?,?,?)", (status.id_str, status.text, status.created_at, status.user.location, (str(status.coordinates)), status.user.followers_count, status.user.friends_count, (str(analysis.sentiment.polarity)))) 
        conn.commit()   
            
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream
#End of reference.

#Starting a stream.
#Code adapted from tweepy documentation.
#Accessed 16/11/18.
#http://docs.tweepy.org/en/v3.5.0/streaming_how_to.html#step-3-starting-a-stream
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Trump'])
#End of reference.