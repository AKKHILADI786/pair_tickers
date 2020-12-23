# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:45:54 2020

@author: AKSHAY KUMAR VERMA
"""

import pandas_datareader.data as pdr
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm  #for mare complex statisical testing
import numpy as np
from statsmodels.tsa.stattools import adfuller  # for adt test

start_date=dt.date.today()-dt.timedelta(200)
end_date=dt.date.today()
ticker="63MOONS.NS"
ticker2="LIKHITHA.NS"


data=pdr.get_data_yahoo(ticker, start_date,end_date,interval='d')
data2=pdr.get_data_yahoo(ticker2, start_date,end_date,interval='d')

plt.subplot(4,1,1)
plt.scatter(data["High"], data2["High"])
plt.subplot(6,1,2)
plt.scatter(data["Low"], data2["Low"])
plt.subplot(6,1,3)
plt.scatter(data["Open"], data2["Open"])
plt.subplot(6,1,4)
plt.scatter(data["Close"], data2["Close"])
plt.subplot(6,1,5)
plt.scatter(data["Volume"], data2["Volume"])
plt.subplot(6,1,6)
plt.scatter(data["Adj Close"], data2["Adj Close"])


ak=data.corrwith(data2,axis=0)

if ak["Adj Close"]<0.75:
    print('corelation test failed')
else:
    print('corelatoin test passed')
    
model=sm.OLS(data["Adj Close"],data2["Adj Close"])
model=model.fit()
a=model.params[0]  # it provode as the hedge ratio

# hedge ratio=stok_1_price/stock_2_price

new_data=pd.DataFrame(data["Adj Close"]-data2["Adj Close"]*a)

x=np.arange(1,138)


plt.plot(x,new_data["Adj Close"])

#check for cointegration of two shares
adf=adfuller(new_data["Adj Close"], maxlag= 1)
adf

# here adf is tuple if adf
#adf[0] gives value of adf test
#adf[4] has a dirctionary if 1% value is less than adf[0] than 99% passed adt test
# if 10% values less than tha 90% passed adt test

if adf[4]["1%"]>adf[0]:
    print('99 % integration test passed')
elif adf[4]["5%"]>adf[0]:
    print('95 % integration test passed')
elif adf[4]["10%"]>adf[0]:
    print('90 % integration test passed')
else:
    print('COintegraion test failed')
    
    

