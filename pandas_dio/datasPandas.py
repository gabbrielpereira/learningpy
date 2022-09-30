import pandas as pd

df1 = pd.read_excel("./datasets/Aracaju.xlsx")
df2 = pd.read_excel("./datasets/Fortaleza.xlsx")
df3 = pd.read_excel("./datasets/Natal.xlsx")
df4 = pd.read_excel("./datasets/Recife.xlsx")
df5 = pd.read_excel("./datasets/Salvador.xlsx")

df = pd.concat([df1, df2, df3, df4, df5])
df["Receita"] = df["Vendas"].mul(df["Qtde"])

df["Data"] = df["Data"].astype("int64")

##Converter para datetime
df["Data"] = pd.to_datetime(df["Data"])

##Agrupar a receita pelo ano
#print(df.groupby(df["Data"].dt.year)["Receita"].sum())

## adicionar Coluna do ano
df["anoVenda"] = df["Data"].dt.year

##adicionar coluna de mês e dia
df["mesVenda"], df["diaVenda"] = df["Data"].dt.month, df["Data"].dt.day

##data mais antiga
print(df["Data"].min())

##diferença entre dias
df["diferencaDias"] = df["Data"] - df["Data"].min()

#criando trimestre
df["trimestreVenda"] = df["Data"].dt.quarter

##Vendas de março 2019
vendasMarco19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.quarter == 4)]
print(vendasMarco19)