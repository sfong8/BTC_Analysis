import pandas as pd


df = pd.read_parquet(r'../Data/cleaned_dataset_20210117.parquet')

###create a new column that is the date column -7
df = df.head(n=100)

from datetime import timedelta

df['NEW_DATETIME'] = df['DATETIME_CONVERTED'].apply(lambda x :x -timedelta(days=7))