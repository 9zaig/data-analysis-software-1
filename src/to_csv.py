import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from sklearn.metrics import r2_score
from lmfit import Model
from extracting import Extract

class Tocsv:
    def __init__(self,data):
        self.data=data
    def mpandas(self):
        cols=["Rsq of IV (1)","I at -1V [A]", "I at 1V [A]","Rsq of Ref.spectrum(Nth)","Max Transmission of Ref.spec.(dB)"]
        row=[]
        for i in range(1,6):
            row.append(self.data[i])
        df = pd.DataFrame(row, columns=cols)
        df_2nd=pd.concat([Extract.extracting_information(),df],axis=1)
        df_2nd.to_csv('.csv')

