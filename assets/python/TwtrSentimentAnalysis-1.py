# Import dependancies
import tweepy
from textblob import TextBlob
import csv

# Name your file
csv_out = open('pizza.csv', 'w')

# Authenticate with Twitter
consumer_key = 'pWfx4N4Cgo8aXJ89bZ48MdTVC'
consumer_secret = '5NtO4texOKXzGIGnOGTWfzqsBX0tK47Lxt8kipivxZHDChhtPP'
access_token = '2315182878-QWMsMerPllvQ665UfGDeIxNPhkb61Wx0TeY01EA'
access_token_secret = 'OJLKImNniqI5CRbKLe6XAHlYJ8OlCw6VQF4qcILuGBAP7'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Create your query
public_tweets = api.search(q='pizza', count=100)

# Create headers
headers = "TWEET" + "," + "POLARITY" + "," + "SUBJECTIVITY" + "\n"
csv_out.write(headers)
scrub = str.maketrans(dict.fromkeys('Sentiment(polarity=subjectivity=)'))
                      
for tweet in public_tweets:
    TXT = (tweet.text)
    print (TXT)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
    out = str(TXT).replace(","," ") + "," + str(analysis.sentiment).translate(scrub) + "\n"
    csv_out.write(out)
       
csv_out.close()


# Wait our csv is messy, let's clean it up

import pandas as pd
data = pd.read_csv('pizza.csv', sep=',')
print (data)
data.dropna()
data.dropna().to_csv('pizza_formatted.csv')

print ("COMPLETE")
