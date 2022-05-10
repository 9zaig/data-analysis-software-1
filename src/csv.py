import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from sklearn.metrics import r2_score
from lmfit import Model

df_cols=["Batch","Wafer","Maskset", "TestSite","Date","Operator", "DieColumn", "DieRow"]
row=[]
for node in root.iter("OIOMeasurement"):
    cdate=node.attrib["CreationDate"]
    coper=node.attrib["Operator"]
for node in root.iter("TestSiteInfo"):
    # print(node.attrib)
    row.append({"Batch":node.attrib["Batch"],"DieColumn":node.attrib["DieColumn"],"DieRow":node.attrib["DieRow"]
                   ,"Maskset":node.attrib["Maskset"],"TestSite":node.attrib["TestSite"]
                   ,"Wafer":node.attrib["Wafer"],"Date":cdate,"Operator":coper})
out_df=pd.DataFrame(row, columns=df_cols)
print(out_df)
b_clos=["Rsq of IV (1)","Rsq of IV (2)","Rsq of IV (3)","I at -1V [A]", "I at 1V [A]"]
b_row=[]
b_row.append({b_clos[0]:r_squre_1,b_clos[1]:r_squre_2,b_clos[2]:r_squre_3,b_clos[3]:equation1(-1)
                 ,b_clos[4]:abs(result.best_fit[3])})
df_b=pd.DataFrame(b_row,columns=b_clos)
print(df_b)
c_clos=["Rsq of Ref.spectrum(Nth)","Max Transmission of Ref.spec.(dB)"]
c_row=[]
c_row.append({c_clos[0]:r_square[5], c_clos[1]:max(polynome[5](x_line))})
df_c=pd.DataFrame(c_row,columns=c_clos)
print(df_c)
Lec09=pd.concat([out_df,df_c,df_b],axis=1)
print(Lec09)
Lec09.to_excel('Lec09_trial.xlsx')

##################################
class tocsv:
    def __init__