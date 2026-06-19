"""
use pandas to operate excel
pip install pandas openpyxl
"""
import pandas as pd
import numpy as np

data = pd.read_excel("data.xlsx")
# print(data)
# filter age
# print(data[data['age']>19])
# filter gender
# print(data[data['Gender']=='female'])
# filter name
# print(data['Name'])
# 
print(max(data['age']))
print(np.mean(data['age']))
minVal = min(data['age'])
data['age'] = data['age'].fillna(minVal) # the inplce = True not working
# print(data)
data2 = data.sort_values(by="age",ascending=False)
# print(data2)

data2.to_excel("data2.xlsx")