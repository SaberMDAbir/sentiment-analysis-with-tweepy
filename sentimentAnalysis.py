import tweepy
from textblob import TextBlob

# api information not present on purpose
# creating four variables that we can use to authenticate twitter
consumer_key = 
consumer_secret = 

access_token = 
access_token_secret = 

# auth with twitter
# log-in via code
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create main api variable to do all twitter magic
api = tweepy.API(auth)

# collect tweets that contain a specific keyword
public_tweets = api.search('Elon')

'''
# prints out to terminal
for tweet in public_tweets:
    print(tweet.text)
    # conduct sentiment analysis. Stores analysis
    analysis = TextBlob(tweet.text)
    # print out sentiment analysis
    print(analysis.sentiment)
'''

'''
Instead of printing out each tweet, save each Tweet to a CSV file with an 
associated label. The label should be either 'Positive' or 'Negative'. You can 
define the sentiment polarity threshold yourself, whatever you think constitutes 
a tweet being positive/negative. 
--------------------------------------------------------------------------------
Approach --> Create a list seperated by tweet and the associated label. Let's
make the label positive when it's .5 and over and negative when it's .49 and 
under
Write that list to the created CSV file by using csvFileName.writerows(list)

Next time, it'd probably be better to use pandas 
'''
tweetData = []
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity >= 0:
        sentimentTweet = "positive"
    else:
        sentimentTweet = "negative"
    mt = [analysis,sentimentTweet]
    tweetData.append(mt)

import numpy as np
myarray = np.asarray(tweetData)

import csv
with open('outputTest.csv','w',newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(myarray)