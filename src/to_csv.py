import numpy as np
import pandas as pd

class Tocsv:
    def __init__(self, data, information_data):
        self.data=data
        self.information_data = information_data

    def mpandas(self):
        cols_data=["Rsq of IV (1)","I at -1V [A]", "I at 1V [A]","Rsq of Ref.spectrum(Nth)","Max Transmission of Ref.spec.(dB)"]
        cols_information=["Batch","Wafer","Maskset", "TestSite","Date","Operator", "DieColumn", "DieRow"]
        row_data=[]
        row_information = []

        row_data.append({cols_data[0]:self.data[0],cols_data[1]:self.data[1],cols_data[2]:abs(self.data[2]),cols_data[3]:self.data[3],cols_data[4]:self.data[4]})

        df_data = pd.DataFrame(row_data, columns=cols_data)
        df_information = pd.DataFrame(self.information_data, columns=cols_information)
        
        df_2nd=pd.concat([df_information,df_data],axis=1)
        #print(df_2nd)
        return df_2nd
    


