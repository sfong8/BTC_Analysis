import pandas as pd


df = pd.read_parquet(r'../Data/cleaned_dataset_20210117.parquet')

###create a new column that is the date column -7
df = df.head(n=100)

from datetime import timedelta

df['NEW_DATETIME'] = df['DATETIME_CONVERTED'].apply(lambda x :x -timedelta(days=1))

##read in the tweets (grouped)

tweets_group = pd.read_parquet(r'../Data/Tweets/tweets_cleaned.parquet')
df['DATETIME_CONVERTED'] = pd.to_datetime(df.DATETIME_CONVERTED, utc = True)

df=df.merge(tweets_group,how='left',on='DATETIME_CONVERTED')
df['TWEET_COUNT'].fillna(0,inplace=True)
