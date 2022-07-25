import pandas as pd 

df1=pd.read_excel("C:\\Users\\User\\Desktop\\python\\joing excel\\Libro1.xlsx")
print(df1)
df2=pd.read_excel("C:\\Users\\User\\Desktop\\python\\joing excel\\Libro2.xlsx")
print(df2)
values1=df1[["codigo","notas"]]
values2=df2[["codigo","notas"]]
dataframes=[values1,values2]
join=pd.concat(dataframes)
join.to_excel("Prueba.xlsx")
