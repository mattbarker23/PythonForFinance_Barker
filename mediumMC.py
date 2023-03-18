import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web

ticker = "MSFT"
startDate = '2018-11-18'
endDate = '2019-11-18'

df = web.DataReader(ticker,'yahoo',startDate,endDate)
df = df[["Close"]]
df['pct'] = df['Close'].pct_change()

histMean = df['pct'].mean()
histStd = df['pct'].std()
print(histStd,histMean)

todayPrice = df["Close"][-1]
print(todayPrice)

timePoints = 41
scenarios = 1000
simulatedCurves = []

for scenarios in range(0,scenarios):
    simulatedPrices = [todayPrice]
    monteCarloMoves = np.random.normal(histMean,histStd,timePoints)

    # print(monteCarloMoves)
    for move in monteCarloMoves:
        previousDayPrice = simulatedPrices[-1]
        nextDayPrice = previousDayPrice*(1+move)
        simulatedPrices.append(nextDayPrice)
    simulatedCurves.append(simulatedPrices)
    days = list(range(0,timePoints+1))
    # plt.plot(days,simulatedPrices)

percentile = np.percentile(simulatedCurves,55,axis=0)
plt.plot(days,percentile,'r--')

dfTest = web.DataReader(ticker,'yahoo',endDate,'2020-01-18')#42 trading days
dfTestPrices = dfTest["Close"].values
plt.plot(days,dfTestPrices)
plt.show()