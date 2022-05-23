import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from sklearn.metrics import r2_score
from lmfit import Model
import extracting

class Tocsv:
    def __init__(self,data):
        self.data=data
    def mpandas(self):
        b_clos=["Rsq of IV (1)","I at -1V [A]", "I at 1V [A]"]
        b_row=[b]
        df_b = pd.DataFrame(b_row, columns=b_clos)
        c_clos=["Rsq of Ref.spectrum(Nth)","Max Transmission of Ref.spec.(dB)"]
        c_row=[]
        df_c = pd.DataFrame(c_row, columns=c_clos)
        df_2nd=pd.concat([extract.extracting_information(),df_c,df_b],axis=1)
    def mcsv(self):
        result.to_csv('.csv')
        data.to_csv('result')
