import pandas as pd
import numpy as np

# pd.concat([df1,df2,...])
df1 = pd.read_excel("./stu1.xlsx",index_col='id')
# print(df1)
df2 = pd.read_excel("./stu2.xlsx",index_col='id')
# print(df2)
df3 = pd.concat([df1,df2],axis=1) #  axis=1 ,join by column
# print(df3)
# df3.to_excel("stu.xlsx")

# pd.merge(df1,df2,...,how='inner',on='id')
df4 = pd.merge(df1,df2,how='inner',on='id')
# print(df4)

# data cleaning
# df_test = pd.read_excel("./test.xlsx",index_col='id')
# # print(df_test.isnull())
# # print(df_test.isna())
# # dropna()
# # df_new = df_test.dropna() # by default ,drop the row
# # print(df_new)
# # df_new = df_test.dropna(axis=1) # by default ,drop the row we can change it to drop the column
# # print(df_new)
# df_new = df_test.fillna(value=0)
# # print(df_new)

# # print(df_test.duplicated('name'))
# # print(df_test.drop_duplicates('name',keep='last'))
# df_test.drop_duplicates('name',keep='last',inplace=True)
# print(df_test)

# preprocess
df_test = pd.read_excel("./test.xlsx",index_col='id',usecols=['id','name','gender','age','email'])
# print(df_test)
print(df_test[df_test.email.str.contains('foobar')])

