#Import files needed to perform operations on data
from DataLoad import load_data
from DatasetAnalysis import analyze_twitter_dataset, analyze_bitcoin_dataset
from DatasetPreparation import prepare_dataset

if __name__ == '__main__':
    dft, dfb = load_data()
    #analyze_twitter_dataset(dft)
    #analyze_bitcoin_dataset(dfb)
    df = prepare_dataset(dft,dfb)

