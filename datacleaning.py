#data_cleaning.py f
import pandas as pd
#load data(example : from a URL or local file)
url = " https://people.sc.fsu.edu/"jburkardt/data/csv/hw_200.csv"
df =pd.read_csv(url)
#cleaning example
df.dropna(inplace=True)
df.columns =[col.strip().lower().replace(
