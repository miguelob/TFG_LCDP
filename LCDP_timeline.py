import tweepy #https://github.com/tweepy/tweepy
import matplotlib.pyplot as plt
import pandas as pd
import configparser
import csv

#Twitter API credentials

config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config['twitter']['api_key']
consumer_secret = config['twitter']['api_key_secret']

access_key = config['twitter']['access_token']
access_secret = config['twitter']['access_token_secret']


def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []  
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print(f"...{len(alltweets)} tweets downloaded so far")
    
    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[ tweet.created_at.strftime("%Y-%m"),tweet.favorite_count,tweet.retweet_count,tweet.text] for tweet in alltweets]
    
    #write the csv  
    with open(f'new_{screen_name}_tweets_text.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["created_at","favorite_count","retweet_count", "text"])
        writer.writerows(outtweets)
    
    pass

    df = pd.read_csv('new_lacasadepapel_tweets.csv')
    ylabels = ["favorite_count","retweet_count"]

    fig = plt.figure(figsize=(13,3))
    fig.subplots_adjust(hspace=0.01,wspace=0.01)

    n_row = len(ylabels)
    n_col = 1
    for count, ylabel in enumerate(ylabels):
        ax = fig.add_subplot(n_row,n_col,count+1)
        ax.bar(df["created_at"],df[ylabel])
        ax.set_ylabel(ylabel)
    plt.show()


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("lacasadepapel")