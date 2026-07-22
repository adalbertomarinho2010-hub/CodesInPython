import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# df.head(5)
# df.tail(5)
# df.info()
# df.index
df.head(12)
df.set_index('PassengerId', inplace= True)
# print(df.columns)
# print(df.loc[1])
# print(df.loc[[1,2,3]])
# print(df.loc[[1,2],["Name","Sex","Age"]])
# df.loc[1:10,["Name","Sex","Age"]]
# x = df.loc[1:10,["Name","Sex","Age"]]
# print(x.query('Age >= 30 & Sex=="male"')) #||| (pipe) = Or (Ou) 
