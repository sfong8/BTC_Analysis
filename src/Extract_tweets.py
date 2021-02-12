import twint



import pandas as pd


start_list = pd.date_range('2020-01-01','2021-01-01',
              freq='MS').strftime("%Y-%m-%d").tolist()

end_list = pd.date_range('2020-02-01','2021-02-01',
              freq='MS').strftime("%Y-%m-%d").tolist()

for i in range(0,len(start_list)):
    start = start_list[i]
    end = end_list[i]
    try:
        outfile = fr'../Data/Tweets/BTC_{start}_{end}.json'
        c = twint.Config()
        c.Since = start
        c.Until = end
        c.Search = '#BTC'
        c.Store_json=True
        c.Output = outfile
        twint.run.Search(c)
    except:
        print(fr'failed - {start}')