import numpy as np
import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from itertools import product

#style.use('ggplot')
paramList = ['PE','PB']
peRange = range(3,8)
pbRange = range(0,3)
epsRange = range(10,50,10)
deRange = range(10,50,10)
fcfRange = range(10,50,10)
roeRange = range(3,5)
roaRange = range(3,5)

df = pd.read_csv('book.csv',
    index_col=0)
    
#Iteration Function 
'''   
numIterations=0
for element in product(peRange,pbRange):
    numIterations=numIterations+1
    print element
print numIterations
'''

dfEmpty = pd.DataFrame({'A' : []})
df = pd.read_csv('book.csv',index_col=0)
dfEmpty.to_csv('pandasOut.csv',mode='w')

#Scoring Function (Long Way)
def ftgscore(df, ranges):
    #Test Ranges
    #peTest = ranges[0]
    #pbTest = ranges[1]
    #testRanges = [peTest, pbTest]
    
    testDict = {'peTest':ranges[0], 'pbTest':ranges[1],'epsTest':ranges[2],
        'deTest':ranges[3],'fcfTest':ranges[4],'roeTest':ranges[5],
        'roaTest':ranges[6]}

    df['PE Score'] = df['PE'] < ranges[0]
    df['PB Score'] = df['PB'] < ranges[1]
    df['EPS Score'] = df['EPS'] > ranges[2]
    df['DE Score'] = df['DE'] < ranges[3]
    df['FCF Score'] = df['FCF'] > ranges[4]
    df['ROE Score'] = df['ROE'] > ranges[5]
    df['ROA Score'] = df['ROA'] > ranges[6]
    df['BETA Score'] = 1.0/(df['BETA']*10000)
    df['FTG Score'] = (df['PE Score'].astype(int) + df['PB Score'].astype(int) \
    + df['EPS Score'] + df['DE Score'] + df['FCF Score'] + df['ROE Score'] +
        df['ROA Score'] + df['BETA Score'])
    
    #Sort Scored Data
    df.sort_values(by=['FTG Score'], ascending=[False], inplace=True)

    #Trim Data to Top 10 Companies
    df = df[:10]
    
    #Add Parameter Columns
    for key, value in testDict.items():
        df.insert(0,('%s Test' % key),(value))
    
    #Get Average Returns of Top 10 Companies
    avgReturn = df['RETURN'].mean()
    df.insert(0,'Avg Return',avgReturn)
    
    #Calculate Sharpe Ratio
    sharpe = (df['RETURN'] / df['RETURN'].std()) * np.sqrt(365.25)
    df.insert(0,'Sharpe',sharpe)
    print sharpe
    
    df = df[:1]
    
    #Output
    outputCSV(df)
    
#Output Function
def outputCSV(df):
    if numIterations==0:
        df.to_csv('pandasOut.csv',mode='a')
    else:
        df.to_csv('pandasOut.csv',mode='a', header=False)

#Iteration Loop
numIterations=0
for ranges in product(peRange,pbRange,epsRange,deRange,fcfRange,roeRange,\
        roaRange):
    ftgscore(df, ranges)
    print ranges
    numIterations=numIterations+1
print numIterations

'''
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
'''