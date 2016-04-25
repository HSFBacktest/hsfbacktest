import numpy as np
import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
import datetime
from itertools import product
#from openpyxl import load_workbook

df = pd.read_excel('DailyData.xlsx',sheetname='Consumer Discretionary',index_col='Date', 
        parse_dates=True)
df.index
start = datetime.datetime(2014,1,2)
end = datetime.datetime(2014,12,31)

df2 = df[start:end]

print(df2.head())

'''
dfs = {sheet_name: xl_file.parse(sheet_name)
        for sheet_name in xl_file.sheet_names}
'''
