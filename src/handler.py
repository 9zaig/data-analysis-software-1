import numpy as np

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