import numpy as np
import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style
from itertools import product

style.use('ggplot')
paramList = ['PE','PB']
peRange = range(0,20)
pbRange = range(0,5)
epsRange = range(0,100,10)
deRange = range(0,100,10)
fcfRange = range(0,100,10)
roeRange = range(0,20)
roaRange = range(0,20)

df = pd.read_csv('/Users/SteveKeyHarvey/OneDrive/Development/HSFBacktest/book.csv',
    index_col=0)
    
#Iteration Function 
'''   
numIterations=0
for element in product(peRange,pbRange):
    numIterations=numIterations+1
    print element
print numIterations
'''

#Scoring Process (Long Way)
df['PE Score'] = df['PE'] < 17
df['PB Score'] = df['PB'] < 4
df['EPS Score'] = df['EPS'] > 0
df['DE Score'] = df['DE'] < 70
df['FCF Score'] = df['FCF'] > 20
df['ROE Score'] = df['ROE'] > 13
df['ROA Score'] = df['ROA'] > 14
df['BETA Score'] = 1.0/(df['BETA']*10000)
df['FTG Score'] = (df['PE Score'].astype(int) + df['PB Score'].astype(int) + 
    df['EPS Score'] + df['DE Score'] + df['FCF Score'] + df['ROE Score'] +
    df['ROA Score'] + df['BETA Score'])

#Sort Scored Data
df2 = df.sort_values(by=['FTG Score'], ascending=[False])
#Trim Data to Top 10 Companies
df3 = df2[:10]
print (df3)



#def iterate(*args):
#    for element in 
#        x = product(*args)
#        print(list(x))
#        print(len(list((x))))

#def ftgScore(Ratio, peRange, pbRange):
#    for score in peRange:
#        print ("E: %d" % score)
#        for score in pbRange:
#            print ("B: %d" % score)

#def ftgScore1(Ratio, Score):
#    df[('%s Score' % Ratio)] = df[('%s' % Ratio)] < Score
#    print(df[('%s Score' % Ratio)])

#for item in paramList:
#ftgScore(paramList[0], peRange, pbRange)

#for x in np.nditer(peRange):
#    print x
  
#print (df.head())
#start = datetime.datetime(2012,1,1)
#end = datetime.datetime(2015,1,1)
#df = web.DataReader("SHPG", "yahoo", start, end)
#print(df[['Adj Close','Close']])
#df['Adj Close'].plot()
#plt.show()