# In this exercise you will be required to calculated the inflation-adjusted values for SP500
# 1. Download "Consumer Price Index for All Urban Consumers: All Items" from Fred from 7/15/1989 to 7/15/2018
# 2. Normailze the original value to inflation-adjusted value, i.e. dollar today = 1$, dollar 10 years would buy 1.25 times as much
# 3. Load the "^spx_d_reind.csv"
# 4. Calculate the inflation-adjusted values of SPX for a given date(that will be monthly)
# 5. Calculate the daily pct change of inflation adjusted SPX for each month
# 6. Plot both adjusted and unadjusted results, name them accordingly
# 7. Plot the pct change values on the histogram with 25 bins
# 8. Upload this file along with two generated images

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import pandas_datareader as wb

fromDate = datetime(1989,7,15)
toDate = datetime(2018,7,15)

inflation = wb.DataReader("CPIAUCSL","fred",fromDate,toDate)

inflation["IA"] = inflation['CPIAUCSL'][-1]/inflation['CPIAUCSL']


SPX = pd.read_csv("^spx_d_reind.csv",index_col="Date",parse_dates=True)
SPX = SPX[ ['Close'] ]
SPX.index.names = ['DATE']

join = inflation.merge(SPX, on="DATE", how="inner")
join.rename(columns={'Close': 'Unadjusted'}, inplace=True)

join["Adjusted"] = join['Unadjusted']*join["IA"]
join["pctChange"] = join["Adjusted"].pct_change()
print(join)

unadj = join["Unadjusted"].values
adj = join["Adjusted"].values
index = join.index

plt.plot(index,unadj,'r',label='Unadjusted Returns')
plt.plot(index,adj,'b',label='Inflation-Adjusted Returns')
plt.legend()
plt.show()

values = join["pctChange"].values
values = values[1:]
plt.hist(values,bins=25,facecolor="red",alpha=0.7)
plt.show()
