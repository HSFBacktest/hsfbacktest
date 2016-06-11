import numpy as np
import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from itertools import product

df = pd.read_csv('ATTMonthlyDataVALUES.csv',
    index_col=0)

print(df.head())