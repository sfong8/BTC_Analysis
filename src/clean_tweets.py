import pandas as pd
to_clean=True
if to_clean:
    tweets = pd.read_csv(r'../Data/Tweets/tweets.csv',sep=";")


    tweets=tweets[['timestamp']]
    tweets['DATETIME_CONVERTED'] = pd.to_datetime(tweets.timestamp)
    # btc_df_grouped = btc_df.groupby(pd.Grouper(key='DATETIME_CONVERTED',freq='10Min')).mean().reset_index()
    ###tweets per 10mins interval
    tweets['TWEET_COUNT']=1
    tweets_grouped= tweets.groupby(pd.Grouper(key='DATETIME_CONVERTED',freq='60Min')).sum().reset_index()
    tweets_grouped = tweets_grouped[tweets_grouped['DATETIME_CONVERTED']>='2016-01-01']
    tweets_grouped.to_parquet(r'../Data/Tweets/tweets_cleaned.parquet')

