# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pylab 
import scipy.stats as stats
import pandas as pd 
import matplotlib.pyplot as plot
from pandas import DataFrame


df = pd.read_csv("HY_Universe_corporate bond.csv")


#plot scatter plot
df_liqscore = df.loc[:,'LIQ SCORE']
df_n_trades = df.loc[:,'n_trades']

plot.scatter(df_liqscore, df_n_trades)

plot.xlabel("Liquid Score") 
plot.ylabel(("Number of Trade")) 
plot.show()


# plot box plot

df_boxplot = df.loc[:, ['weekly_mean_volume', 'weekly_median_volume', 
                    'weekly_max_volume', 'weekly_min_volume']]
df_boxplot.boxplot(column = ['weekly_mean_volume', 'weekly_median_volume', 
                    'weekly_max_volume', 'weekly_min_volume'])
plot.show()



#plot histogram
plot.hist(df['Client_Trade_Percentage'])
plot.title('Histogram of Client Trade Percentage')
plot.xlabel('Client Trade Percentage')
plot.ylabel('Count')
plot.show()


#plot qq-plot

df_weeklymeanvolume = df.loc[:,'weekly_mean_volume']
stats.probplot(df_weeklymeanvolume, dist="norm", plot=pylab)
plot.title("Quantile‐quantile plot of Weekly Mean Volume")
plot.show()

#plot heat map
corMat = DataFrame(df.iloc[:,20:29].corr())
plot.pcolor(corMat)
plot.title("Heat Map")
plot.show()

print("My name is {Xuebin Wang}")
print("My NetID is: {xuebinw2}")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")





