# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib import style
#import csv
#data_file=pd.read_csv ('trade_count.csv')
#print (data_file[0:7])

palette = plt.get_cmap('Set1')
plt.style.use ('seaborn-darkgrid')

Hour,TradeCount = np.loadtxt('trade_count.csv', unpack = True,delimiter = ',') 
plt.plot(Hour,TradeCount, label='Hourly Trade Count')
plt.xlabel('Hour')
plt.ylabel('TradeCount')

fig1 = plt.gcf() 

#fig1 = plt.figure(figsize=(8, 8))
plt.show() 
plt.draw()
fig1.savefig('trade_count.png', dpi=500)
