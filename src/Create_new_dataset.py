import pandas as pd
import numpy as np

btc_df = pd.read_csv(r"../Data/bitstampUSD_1-min_data_2012-01-01_to_2020-12-31.csv")
###get the head first 5000

# btc_df = btc_df.head(n=5000)

###check the types of the columns
btc_df.dtypes
btc_df.describe()
btc_df.info()
from datetime import datetime

btc_df['DATETIME_CONVERTED'] = pd.to_datetime(btc_df.Timestamp,unit='s')

# btc_df.to_csv('../Data/bitstampUSD_1-min_data_2012-01-01_to_2020-12-31_cleaned.csv',index=None)


btc_df2 = btc_df[btc_df['DATETIME_CONVERTED']>='2016-01-01']

btc_df2.to_csv('../Data/bitstampUSD_1-min_data_2012-01-01_to_2020-12-31_cleaned.csv',index=None)
btc_df2.isna().sum()


import pandas as pd
import numpy as np

btc_df = pd.read_csv(r"../Data/bitstampUSD_1-min_data_2012-01-01_to_2020-12-31_cleaned.csv")
###get the head first 5000

# btc_df = btc_df.head(n=5000)

###check the types of the columns
btc_df.dtypes
btc_df.describe()
btc_df.info()
from datetime import datetime

btc_df['DATETIME_CONVERTED'] = pd.to_datetime(btc_df.DATETIME_CONVERTED)

###lets do it for 10mns interval
x = btc_df.head(n=10)

btc_df_grouped = btc_df.groupby(pd.Grouper(key='DATETIME_CONVERTED',freq='60Min')).mean().reset_index()

###fill the na values in the volume column as 0.0
btc_df_grouped['Volume_(BTC)'].fillna(0.0,inplace=True)
btc_df_grouped['Volume_(Currency)'].fillna(0.0,inplace=True)

cols_to_fill = ['Open', 'High', 'Low', 'Close', 'Weighted_Price']
for col in cols_to_fill:
    btc_df_grouped[col].fillna(method='ffill',inplace=True)

from matplotlib import pyplot

# btc_df_grouped[['Weighted_Price','DATETIME_CONVERTED']].plot()
# pyplot.show()


##use tyhe weighted price for noce
btc_df_grouped2 = btc_df_grouped[['DATETIME_CONVERTED', 'Volume_(BTC)', 'Weighted_Price']]

btc_df_grouped2.to_parquet(r'../Data/cleaned_dataset_20210117.parquet')