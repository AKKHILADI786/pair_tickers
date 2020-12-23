# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:10:44 2020

@author: AKSHAY KUMAR VERMA
"""

import pandas_datareader.data as pdr   # for import data from yahoo finance
import datetime as dt   #for date and time purpose
import matplotlib.pyplot as plt

start_date=dt.date.today()-dt.timedelta(365)
end_date=dt.date.today()
ticker="SBIN.NS"


data=pdr.get_data_yahoo(ticker, start_date,end_date,interval='m')


plt.scatter(data["High"], data["Low"])