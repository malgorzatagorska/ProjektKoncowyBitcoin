import seaborn as sns
def explore(df):
    #show_correlation(df)
    return

def show_correlation(df):
    print('Correlation matrix:')
    df = df.drop(columns=['date', 'user', 'text'])
    print(df.head())

    corr = df.corr()
    sns.heatmap(corr,
                xticklabels=corr.columns,
                yticklabels=corr.columns)