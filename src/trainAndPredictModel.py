import pandas as pd


df = pd.read_parquet(r'../Data/cleaned_dataset_20210117.parquet')

###create a new column that is the date column -7
# df = df.head(n=100)

from datetime import timedelta

df['NEW_DATETIME'] = df['DATETIME_CONVERTED'].apply(lambda x :x -timedelta(days=1))

##read in the tweets (grouped)

tweets_group = pd.read_parquet(r'../Data/Tweets/tweets_cleaned.parquet')
df['DATETIME_CONVERTED'] = pd.to_datetime(df.DATETIME_CONVERTED, utc = True)

df=df.merge(tweets_group,how='left',on='DATETIME_CONVERTED')
df['TWEET_COUNT'].fillna(0,inplace=True)
df.columns = ['DATETIME_CONVERTED', 'Volume_(BTC)', 'y', 'ds',
       'TWEET_COUNT']
###split the data 20-80%
###number of rows
rows = int(df.shape[0]*0.8)

train_df = df[:rows]
test_df = df[rows:]

from datetime import datetime
from fbprophet import Prophet
print(datetime.now())
df_prophet = Prophet(changepoint_prior_scale=0.15, daily_seasonality=True)
df_prophet.fit(train_df)

fcast_time=144   # 1 year

print(datetime.now())
df_forecast = df_prophet.make_future_dataframe(periods= fcast_time, freq='10min')
df_forecast.tail(10)


df_forecast = df_prophet.predict(df_forecast)

import pickle
pickle.dump( df_prophet, open( "prophet_model.pickle", "wb" ) )
# df_forecast.to_parquet('../Data/df_forcast.parquet')
forecast=df_forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
fig1 = df_prophet.plot(forecast)
fig1.show()