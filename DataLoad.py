import os
import pandas as pd

#function loading the data to a dataframe
def load_data():
    twitter_path = 'C:\\Users\\atago\\PycharmProjects\\ProjektKoncowy\\datasets\\tweets.csv'
    twitter_columns = ['user', 'fullname', 'url', 'timestamp', 'replies', 'likes', 'retweets', 'text']
    bitcoin_path = 'C:\\Users\\atago\\PycharmProjects\\ProjektKoncowy\\datasets\\BTC-USD.csv'
    bitcoin_columns = ['Date', 'Adj Close', 'Volume']

    dft = load_twitter_data(twitter_path, twitter_columns)
    dfb = load_bitcoin_data(bitcoin_path, bitcoin_columns)
    return dft, dfb

def load_twitter_data(path, columns):
    #df = pd.read_csv(path, sep=';', skiprows=[i for i in range(1,1500000)], usecols = columns, low_memory=False)
    df = pd.read_csv(path, sep=';', nrows= 15000, usecols=columns, low_memory=False)
    return df

def load_bitcoin_data(path, columns):
    df = pd.read_csv(path, sep=',', usecols = columns)
    return df