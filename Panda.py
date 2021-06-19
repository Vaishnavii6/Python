import pandas as pd
import numpy as np

# mydataset={'cars':["BMW","Audi","Ford"],
#            'passings':[3,4,5]}
#
# new=pd.DataFrame(mydataset)
# print(new)

# Pandas Series

# a=[1,5,2]
# new=pd.Series(a)
# print(new)
# print(new[2])
# newind=pd.Series(a,index=["x","y","z"])
# print(newind)
# print(newind["y"])

# calories={"day1":420,"day2":520,"day3":320}
# myvar=pd.Series(calories)
# print(myvar)
# myvar=pd.Series(calories,index=["day1"])
# print(myvar)

# DataFrames

# data={"calories":[420,530,380],"duration":[10,20,30]}
# myvar=pd.DataFrame(data)
# print(myvar)
# print(myvar.loc[1])
# print(myvar.loc[[0,2]])

# Pandas Read CSV

# df=pd.read_csv('data.csv')
# # print(df)
# print(df.to_string())

dict1={
    "name":["abc","xyz","pqr","stu"],
    "marks":[92,12,34,45],
    "city":["nagpur","delhi","akola","mumbai"]
}
# df=pd.DataFrame(dict1)
# print(df)
# df.to_csv('friends.csv')
# df.to_csv('index.csv',index=False)
# print(df.head(2))
# print(df.tail(2))
# print(df.describe())

df=pd.read_csv('friends.csv')
# print(df)
# print(df['marks'])
# print(df['marks'][0])
# print(df['marks'][0])

# print(type(df['marks']))
# print(type(df))

#SERIES

# ser=pd.Series(np.random.rand(34))
# print(ser)

#DATAFRAME

df=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
# print(df.head())
# print(df)
# print(df.dtypes)
# df[0][0]="vaishnavi"
# print(df.head())
# print(df.dtypes)

# print(df.to_numpy())                   #Array form

# print(df.T)                     #Transpose

# print(df.sort_index(axis=0,ascending=False))               #sorted in row

# print(df.sort_index(axis=1,ascending=False))                 #sorted in column

# newdf=df                               #This is a view
# newdf[0][0]=973
# print(df)

# newdf=df.copy()                               #This is a copy
# newdf[0][0]=9734
# print(df)

# df.loc[0,0]=654
# print(df.head(2))

# print(df.loc[[1,2],[1,2]])

# print(df.loc[:,[1,2]])

# print(df.loc[[1,2],:])

# print(df.loc[(df[0]<0.2)])

# print(df.loc[(df[0]<0.2) & (df[2]>0.3)])

# print(df.iloc[0,4])

# print(df.drop([0]))                      #delete the row

# df.drop([0],axis=1,inplace=True)                 #delete the column
# print(df)
#
# df.drop([1,5],axis=0,inplace=True)
# print(df)
#
# df.reset_index(drop=True,inplace=True)
# print(df.head(5))

df.loc[:,[2]]=None
# print(df[2])
print(df[2].isnull())
