import pandas as pd

df1 = pd.read_excel("./datasets/Aracaju.xlsx")
df2 = pd.read_excel("./datasets/Fortaleza.xlsx")
df3 = pd.read_excel("./datasets/Natal.xlsx")
df4 = pd.read_excel("./datasets/Recife.xlsx")
df5 = pd.read_excel("./datasets/Salvador.xlsx")

#print(df1.head())

##junta arquivos
df = pd.concat([df1, df2, df3, df4, df5])

##primeiras linhas
#print(df.head())

##ultimas linhas
#print(df.tail())

##amostra do conjunto
#print(df.sample(5))

##tipo de dados
#print(df.dtypes)

##alterar tipo do dado da coluna
#df["LojaID"] = df["LojaID"].astype("object")
#print(df.dtypes)

##linhas com valores faltantes
#print(df.isnull().sum())

##substituir valores nulos por média
#df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)
#print(df["Vendas"].mean())

###substituir por zero
#df["Vendas"].fillna(0, inplace=True)

##apagar linhas nulas
#df.dropna(inplace=True)

##apagar nulos baseados em apenas 1 coluna
#df.dropna(subset=["Vendas"], inplace=True)

##Remover  linhas que estejam com valores faltantes em todas as colunas
#df.dropna(how="all", inplace=True)

###CRIAR NOVAS COLUNAS

##criar coluna receitas
df["Receita"] = df["Vendas"].mul(df["Qtde"])
#print(df.head())

##coluna receita/vendas
#df["Receita/Vendas"] = df["Receita"]/df["Vendas"]

##maior receita
#print(df["Receita"].max())

##menor receita
#print(df["Receita"].min())

##maiores receitas
#print(df.nlargest(3,"Receita"))

##menores receitas
#print(df.nsmallest(3,"Receita"))

##Agrupamento por cidade
#print(df.groupby("Cidade")["Receita"].sum())

##ordernar

print(df.sort_values("Receita", ascending=False).head(10))