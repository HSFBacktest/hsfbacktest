import numpy as np
import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
import datetime as dt
from itertools import product

def ExcelDateToDateTime(xlDate):
    epoch = dt.datetime(1899, 12, 30)
    delta = dt.timedelta(hours = round(xlDate*24))
    return epoch + delta

df = pd.read_excel(io='DailyData.xlsx',sheetname='Consumer Discretionary',index_col=0)

df.

start = datetime.datetime(2014,1,2)
end = datetime.datetime(2014,12,31)


print(df['Date'])

#df['Date'] = df['Date'].apply(ExcelDateToDateTime)

#print(df.head())




#df = pd.DataFrame.from_csv('DailyDataCSV.csv',index_col=0)




'''
start = datetime.datetime(2014,1,2)
end = datetime.datetime(2014,12,31)

df = pd.read_excel(filename='DailyData.xlsx',sheetname='Consumer Discretionary')

'''
'''
dfs = {sheet_name: xl_file.parse(sheet_name)
        for sheet_name in xl_file.sheet_names}
'''
