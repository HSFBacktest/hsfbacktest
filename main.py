import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

start = datetime.datetime(2012,1,1)
end = datetime.datetime(2015,1,1)

df = web.DataReader("SHPG", "yahoo", start, end)


print(df.tail(1))
df['Adj Close'].plot()

#plt.show()