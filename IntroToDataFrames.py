import openpyxl as openpyxl
import pandas_datareader.data as wb
import datetime as date
#Step 1(10 points): Remotely Download "Treasury Constant Maturity Rate" from FRED
#(https://fred.stlouisfed.org/categories/115) from 02/01/2014 to 02/01/2016:
#6-Month
#1-Year
#5-Year
#10-Year
#Step 2( 5 points ): Determine the average and standard deviation for each of the maturities( maturity is 6-month, 1 year, etc.)
#Step 3( 5 points ): Select only those rows that have value more or less than avg +/- 1 std
#Step 4( 10 points ): Create a dataframe which has only those rows for which all of the maturities
#has value outside of avg +/- 1 std. Hint: think about joins for frames in step 3
#Step 5( 5 points): Save the generated dataframe as sigma.xlsx
#Please upload this filled file and sigma.xlsx

import pandas_datareader.data as wb
import pandas as pd
import datetime as date

fromDate = "2014-02-01"
toDate = "2016-02-01"

df = wb.DataReader("DGS6MO","fred",fromDate,toDate)
df.rename(columns={'DGS6MO': '6-Month'}, inplace=True)
df[ "1-Year" ] = wb.DataReader("DGS1","fred",fromDate,toDate)
df[ "5-Year" ] = wb.DataReader("DGS5","fred",fromDate,toDate)
df[ "10-Year" ] = wb.DataReader("DGS10","fred",fromDate,toDate)

means = df.mean()
stdevs = df.std()

newdf = df[ (df >= means + stdevs) | (df <= means - stdevs) ]
newdf = newdf.apply (pd.to_numeric, errors='coerce')
newdf = newdf.dropna()
print(newdf)

newdf.to_excel('sigma.xlsx', index = True)