import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def describ():
    pa=pd.read_csv('EOD-DIS.csv')
    print(pa)
    print(" the values  : ",pa.columns.values)
    print(pa.describe())
    print(pa[["Open"]].max())
    print(pa[["High"]].count())
    print(pa[["Adj_Close"]].std())
    print(pa[["Low"]].min())
    print(pa[["Adj_Volume"]].mean())
def mat_plot():
    print(plt.plot(pa[["Open","High","Low","Close",
                       "Volume","Dividend","Split",
                       "Adj_Open","Adj_High","Adj_Low"]]))
    plt.title('The Walt Disney Company (DIS) Stock Prices, Dividends and Splits')
    plt.xlabel("x")
    plt.ylabel("y")
def sub_plot():
    fig,ax=plt.subplots(figsize=(14,4))
    ax.plot(pa[["Open","High","Low","Close",
                       "Volume","Dividend","Split",
                       "Adj_Open","Adj_High","Adj_Low",
                       "Adj_Close","Adj_Volume","Adj_Close",
                       "Adj_Volume"]])
    plt.title('The Walt Disney Company (DIS) Stock Prices, Dividends and Splits')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

print('''To show Describe enter(desc)
To show matplot enter( plt)
To show subplote enter (sup)''')
x=input("enter here =  ")
if x=='desc':
    print(describ())
elif x=='plt':
    print(mat_plot())
elif x=='sup':
    print(sub_plot())
else:
    print("not vaild")
