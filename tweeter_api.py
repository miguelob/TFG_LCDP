from math import factorial
from numpy import result_type
import tweepy
import configparser
import pandas as pd
import matplotlib.pyplot as plt
import datetime


# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth, wait_on_rate_limit=True)
search_words = "#LCDP1"
tweets = tweepy.Cursor(api.search_tweets,
                   q=search_words,
                   lang="es").items(10000)


#public_tweets = api.home_timeline()

# create dataframe
print(tweets)
columns = ['Date','RT','Fav', 'Tweet']
data = []
for tweet in tweets:
    data.append([tweet.created_at.strftime("%Y-%m"), tweet.retweet_count, tweet.favorite_count, tweet.text])
    print("texto :"+tweet.text)

df = pd.DataFrame(data, columns=columns)

df.to_csv('lcdp1_test.csv')

labels = ["RT","Fav"]

fig = plt.figure(figsize=(13,3))
fig.subplots_adjust(hspace=0.01,wspace=0.01)

n_row = 2
n_col = 1
for count, ylabel in enumerate(labels):
    ax = fig.add_subplot(n_row,n_col,count+1)
    ax.plot(df["Date"],df[ylabel])
    ax.set_ylabel(ylabel)
plt.show()


