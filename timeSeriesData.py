import numpy as np
import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
import datetime
from matplotlib import style
from itertools import product


df = pd.read_csv('dailyReturns.csv',index_col=0)

print(df)