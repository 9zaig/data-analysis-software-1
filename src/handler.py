import numpy as np

def func(x,a,b,c,d):
    return a*np.exp((x-b)/c)+d

def r_square(y, y_pred):
    y_bar = np.sum(y)/len(y)
    ssreg = np.sum((ypred-ybar)**2)
    sstot = np.sum((y- ybar)**2)
    return ssreg/sstot