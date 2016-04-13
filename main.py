import numpy as np
import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
paramList = ['PE','PB']

df = pd.read_csv('/Users/SteveKeyHarvey/OneDrive/Development/HSFBacktest/book.csv',
    index_col=0)

df['PE Score'] = df['PE'] > 10

def ftgScore(Ratio, Score):
    df[('%s Score' % Ratio)] = df[('%s' % Ratio)] < Score
    print(df[('%s Score' % Ratio)])

for param in paramList:
    ftgScore(param, 8)

#print (df.head())
#start = datetime.datetime(2012,1,1)
#end = datetime.datetime(2015,1,1)
#df = web.DataReader("SHPG", "yahoo", start, end)
#print(df[['Adj Close','Close']])
#df['Adj Close'].plot()
##plt.show()