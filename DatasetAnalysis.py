import pandas as pd

#function to get the info on the existing dataset
def analyze_twitter_dataset(df):
    print('\nAnalyzing Twitter dataset')
    get_basic_info(df)
    get_null_stats(df)
    get_dates_info(df, 'timestamp')
    unique_values_count(df)

def analyze_bitcoin_dataset(df):
    print('--------------------------------')
    print('\nAnalyzing bitcoin dataset')
    get_basic_info(df)
    get_null_stats(df)
    get_dates_info(df, 'Date')
    unique_values_count(df)


def get_basic_info(df):
    print('\nBasic info')
    print(f'Columns: {df.columns.values}')
    print(df.head())
    print(df.info())


def get_null_stats(df):
    print('\nNumber of null values in columns')
    for c in df.columns.values:
        print(f'column {c}: {df[c].isna().sum()}')

def get_dates_info(df, datecol):
    print('\nDataset timeframe')
    print(df[datecol].min())
    print(df[datecol].max())

def unique_values_count(df):
    print('\nUnique values count:')
    print(df.nunique())