import pandas as pd
from datetime import timedelta

from datetime import datetime
from fbprophet import Prophet

df_forecast=pd.read_parquet('../Data/df_forcast.parquet')

import pickle
# df_prophet = pickle.load(open("prophet_model.p",'rb'))
with open('prophet_model.pickle', 'rb') as handle:
    df_prophet = pickle.load(handle)

forecast=df_forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
fig1 = df_prophet.plot(forecast)