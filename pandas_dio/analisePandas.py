import pandas as pd
import matplotlib.pyplot as plt


plt.style.use("seaborn")

df = pd.read_excel("./datasets/AdventureWorks.xlsx")

##tipo dos dados
# print(df.dtypes)

##somatório das vendas
#print(df["Valor Venda"].sum())

##custo total
df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])
#print(round(df["Custo"].sum(), 2))

##lucro
df["Lucro"] = df["Valor Venda"] - df["Custo"]

##llucro total
#print(round(df["Lucro"].sum(), 2))
#print(df.head(1))

##tempo de envio

#df["tempoEnvio"] = df["Data Envio"] - df["Data Venda"]
#print(df["tempoEnvio"])

##média tempo de envio por marca
df["tempoEnvio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
#print(df.groupby(["Marca"])["tempoEnvio"].mean())

##analisando valores ausentes
#print(df.isnull().sum())

##lucro por ano por marca
pd.options.display.float_format = '{:20,.2f}'.format

#print(df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum())

##resetando index
lucroAno = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
#print(lucroAno)

##Qual o total de produtos vendidos
#print(df.groupby(["Produto"])["Quantidade"].sum().sort_values(ascending=False))

##grafico dos produtos vendidos
#df.groupby(["Produto"])["Quantidade"].sum().sort_values(ascending=True).plot.barh()
#plt.show()

##lucro x ano

#df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar()
#plt.show()

##apenas vendas de 2009
# df2009 = df[df["Data Venda"].dt.year == 2009]
# df2009.groupby(df2009["Data Venda"].dt.month)["Lucro"].sum().plot()
# plt.show()

##marca x lucro

# df.groupby(["Marca"])["Lucro"].sum().plot.bar()
# plt.xticks(rotation="horizontal")
# plt.show()

##lucro x classe
# df.groupby(["Classe"])["Lucro"].sum().plot.bar()
# plt.xticks(rotation="horizontal")
# plt.show()

##analises estatisticas
#print(df["tempoEnvio"].describe())

##gráfico boxplot
# plt.boxplot(df["tempoEnvio"])
# plt.show()

##histograma
#plt.hist(df["tempoEnvio"])
#plt.show()

##identificando outlier
#print(df[df["tempoEnvio"] == 20])

df.to_csv("df_vendas_novo.csv", index=False)