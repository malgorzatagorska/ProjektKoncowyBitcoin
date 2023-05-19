import pandas as pd
import numpy as np


def prepare_dataset(dft, dfb):
    #timestamps to dates conversion
    dft['date'] = pd.to_datetime(dft.timestamp, utc=True).dt.date
    dfb['date'] = pd.to_datetime(dfb.Date, utc=True).dt.date

    dft = join_tweets_from_one_day(dft)
    df = get_same_date_range(dft, dfb)
    columns = ['date', 'user', 'text', 'replies', 'likes', 'retweets', 'Adj Close', 'Volume']
    df = pd.DataFrame(df, columns=columns)
    df.rename(columns={'Adj Close': 'bitcoin_price'}, inplace=True)
    df.rename(columns={'Volume': 'bitcoin_volume'}, inplace=True)
    df = get_trend(df)

    return df

def get_same_date_range(dft, dfb):
    #print('Start dates candidates: ' + dft['date'].min() + ', ' + dfb['date'].min())
    #print('End dates candidates: ' + dft['date'].max() + ', ' + dfb['date'].max())

    startdate = dft['date'].min() if dft['date'].min() > dfb['date'].min() else dfb['date'].min()
    print(f'Start date: {startdate}')
    enddate = dft['date'].max() if dft['date'].max() < dfb['date'].max() else dfb['date'].max()
    print(f'End date: {enddate}')

    df = pd.merge(dft, dfb, how='inner', on = 'date')
    return df

def join_tweets_from_one_day(df):
    df['date'] = pd.to_datetime(df.timestamp, utc=True).dt.date
    df['text'] = str(df['text'])
    text_concat_df = df[['date', 'text']]
    text_concat_df = text_concat_df.groupby(['date'], as_index=False).agg({'text': ' '.join})

    replies_sum_df = df[['date', 'replies']]
    replies_sum_df = replies_sum_df.groupby(['date'])['replies'].sum()
    likes_sum_df = df[['date', 'likes']]
    likes_sum_df = likes_sum_df.groupby(['date'])['likes'].sum()
    retweets_sum_df = df[['date', 'retweets']]
    retweets_sum_df = retweets_sum_df.groupby(['date'])['retweets'].sum()

    df = pd.merge(text_concat_df, replies_sum_df, how='inner', on='date')
    df = pd.merge(df, likes_sum_df, how='inner', on='date')
    df = pd.merge(df, retweets_sum_df, how='inner', on='date')

    return df


# method for classification
def get_trend(df):
    df['bitcoin_trend'] = 'new'
    for i in range(len(df)):
        if i==0:
            print('up')
            df.loc[i, 'bitcoin_trend'] = 1
        elif df.loc[i, 'bitcoin_price'] - df.loc[i-1, 'bitcoin_price']  > 0:
            df.loc[i, 'bitcoin_trend'] = 1
        else:
            df.loc[i, 'bitcoin_trend'] = 0
    return df