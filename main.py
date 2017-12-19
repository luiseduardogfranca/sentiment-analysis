from textblob import TextBlob as tb
import tweepy
import numpy as np


#type with your informations of Twitter
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"

access_token = "YOUR_TOKEN_ACCESS"
access_token_secret = "YOUR_TOKEN_SECRET"

#authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#search for tweets with keyword or hashtag
def analisys(keyword):
    public_tweets = api.search(keyword)

    analisys = []
    
    for tweet in public_tweets:

        print("\nTweet:", tweet.text, "\tPolarity:", tb(tweet.text).sentiment.polarity)
        
        #uses TextBlob for sentiment analysis in tweet
        analisys.append(tb(tweet.text).sentiment.polarity)

    print("\nAverage of sentiment:", str(np.mean(analisys)))


text = " "

while (text != ""):
    print("\nType the keyword or hashtag for search in Twitter! ")
    text = input("Type it (press ENTER for exit): ")
    
    if (text != ""):
        analisys(text)
