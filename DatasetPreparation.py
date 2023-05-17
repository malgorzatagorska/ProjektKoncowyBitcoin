import pandas as pd


def prepare_dataset(dft, dfb):
    df = get_same_date_range(dft, dfb)
    columns = ['date', 'user', 'text', 'replies', 'likes', 'retweets', 'Adj Close', 'Volume']
    df = pd.DataFrame(df, columns=columns)
    df.rename(columns={'Adj Close': 'bitcoin_price'}, inplace=True)
    df.rename(columns={'Volume': 'bitcoin_volume'}, inplace=True)

    print(df)
    return df

def get_same_date_range(dft, dfb):
    startdate = dft['timestamp'].min() if dft['timestamp'].min() > dfb['Date'].min() else dfb['Date'].min()
    print(f'Start date: {startdate}')
    enddate = dft['timestamp'].max() if dft['timestamp'].max() < dfb['Date'].max() else dfb['Date'].max()
    print(f'End date: {enddate}')

    dft['date'] = pd.to_datetime(dft.timestamp, utc=True).dt.date
    dfb['date'] = pd.to_datetime(dfb.Date, utc=True).dt.date
    df = pd.merge(dft, dfb, how='inner', on = 'date')

    return df