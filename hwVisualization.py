import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import yfinance as yf

#pick any date after January of 2010
#let's pretend that you had $1000 dollars to invest at that date
#how much would it be today if you have invested back then and sold in on 1st of April 2019
#remotely download the SPX index from your date to 1st of April 2019
#load the FTSE from the file, and select values from your date  to 1st of April 2019
#normalize the return of each index for "Close" column so you can calculate your total return at any given date
#"invest" $1000 dollars on your date and make sure that you show your total gain/loss at every date
#plot both "investments" in SPX and FTSE on the same graph with names of "US Returns" and "EUR Returns" respectively.


fromDate = '2011-03-23'
toDate = '2019-04-01'
NAV = 1000

SPX = yf.download('^GSPC', fromDate, toDate)
SPX = SPX[ ['Close'] ]

FTM = pd.read_csv("^ftm_d.csv", index_col=["Date"], parse_dates=True)
FTM = FTM.loc[fromDate : toDate]
FTM = FTM[ ['Close'] ]

SPX['pctChange'] = SPX['Close'] / SPX['Close'][0]
FTM['pctChange'] = FTM['Close'] / FTM['Close'][0]

SPX['SPXReturn'] = SPX['pctChange']*NAV
FTM['FTMReturn'] = FTM['pctChange']*NAV

join = SPX.merge(FTM, on="Date", how="inner")

SPXY = join["SPXReturn"].values
FTMY = join["FTMReturn"].values
index = join.index

plt.plot(index,SPXY,'r',label='US Returns')
plt.plot(index,FTMY,'b',label='EUR Returns')
plt.legend()
plt.show()
