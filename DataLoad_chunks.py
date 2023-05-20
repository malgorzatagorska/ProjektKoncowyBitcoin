import pandas as pd

twitter_path = 'C:\\Users\\wcwik02\\Desktop\\SDA\\PROJEKT_KOŃCOWY\\datasets\\tweets.csv'
twitter_columns = ['user', 'fullname', 'url', 'timestamp', 'replies', 'likes', 'retweets', 'text']
bitcoin_path = 'C:\\Users\\wcwik02\\Desktop\\SDA\\PROJEKT_KOŃCOWY\\datasets\\BTC-USD.csv'
bitcoin_columns = ['Date', 'Adj Close', 'Volume']

chunks = []
chunksize = 1000000

for chunk in pd.read_csv(twitter_path, chunksize=chunksize, sep=';', usecols=twitter_columns, on_bad_lines='skip',engine='python'):
    chunks.append(chunk)


