import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from sklearn.metrics import r2_score
from lmfit import Model

class tocsv:
    def __init__(self,path):
        self.path=path


    def mcsv(self):
        tree = ET.parse('C:/Users/Csub/PycharmProjects/HY202103 (2)/D07/20190715_190855/HY202103_D07_(0,0)_LION1_DCM_LMZC.xml')
        root = tree.getroot()
        df_cols = ["Batch", "Wafer", "Maskset", "TestSite", "CreationDate", "Operator", "DieColumn", "DieRow",
                   "Rsq of Ref.spectrum(Nth)", "Max Transmission of Ref.spec.(dB)", "Rsq of IV", "I at -1V [A]",
                   "I at 1V [A]"]
        Lot = tree.find("./TestSiteInfo").get('Batch')
        Wafer = tree.find("./TestSiteInfo").get('Wafer')
        Mask = tree.find("./TestSiteInfo").get('Maskset')
        Column = tree.find("./TestSiteInfo").get('Diecolumn')
        Row = tree.find("./TestSiteInfo").get('DieRow')
        TestSite = tree.find("./TestSiteInfo").get('TestSite')
        Date = root.get('CreationDate')
        Operator = root.get('Operator')
        row=[Lot, Wafer,Mask,TestSite,Date,Operator,Column,Row]
        df=pd.DataFrame(columns=df_cols)
        df.loc[0]=row
        # need function for getting rsq, best fit,