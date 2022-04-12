from ctypes.wintypes import LANGID
import tweepy
import pandas as pd

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAErgaQEAAAAAiNoetPakuYQ%2BaTW2t%2BEZMgxetqI%3DwGA65oWGxc2KbRwwZxh3WM1GxCRBvPP0d46sRjovDN91NQDKZ4')

# Replace with your own search query
query = ['La casa de papel']

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at', 'public_metrics'], max_results=100)

# create dataframe
columns = ['Time', 'Tweet', 'Retweets', 'Replies', 'Likes', 'Quotes']
data = []
for tweet in tweets.data:
    data.append([tweet["created_at"],tweet.text,tweet["public_metrics"]["retweet_count"],tweet["public_metrics"]["reply_count"],tweet["public_metrics"]["like_count"],tweet["public_metrics"]["quote_count"]])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv')