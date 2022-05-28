import numpy as np
import pandas as pd

def func(x,a,b,c,d):
    return a*np.exp((x-b)/c)+d

def r_square(y, y_pred):
    y_bar = np.sum(y)/len(y)
    ssreg = np.sum((y_pred-y_bar)**2)
    sstot = np.sum((y- y_bar)**2)
    return ssreg/sstot

def Current_value(X,equation):
    current = equation(X)
    return current

def Current_value_lmfit(X,fit):
    current = fit[X]
    return current

def Max_transmission(X,equation,order:int):
    result = max(equation[order](X))
    return result

def final_csv(df_list):
    #print(df_list)
    final_df = pd.DataFrame()
    for i in range(len(df_list)):
        final_df = pd.concat([final_df,df_list[i]], axis=0)
    final_df.reset_index(drop = True, inplace = True)
    return final_df

def making_csv(final_df):
    final_df.to_csv('./../res/csv/data_analysis.csv')