import numpy as np
import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from itertools import product

df = pd.read_csv('ATTMonthlyDataVALUES.csv',
    index_col=0)

price2 = df['PRICE']
df.insert(0,'PRICE2',price2)

df.PRICE2 = df.PRICE2.shift(-1)

priceReturn = df['PRICE2'] - df['PRICE']
df.insert(0,'RETURN',priceReturn)

returnPercent = df['RETURN']/df['PRICE']*100
df.insert(0,'PERCENTRETURN',returnPercent)

#print(df)
print(df.index)

