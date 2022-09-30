import pandas as pd
import matplotlib.pyplot as plt


df1 = pd.read_excel("./datasets/Aracaju.xlsx")
df2 = pd.read_excel("./datasets/Fortaleza.xlsx")
df3 = pd.read_excel("./datasets/Natal.xlsx")
df4 = pd.read_excel("./datasets/Recife.xlsx")
df5 = pd.read_excel("./datasets/Salvador.xlsx")

df = pd.concat([df1, df2, df3, df4, df5])

df["Receita"] = df["Vendas"].mul(df["Qtde"])
df["mesVenda"] = df["Data"].dt.month

##lista com vendas por loja
#print(df["LojaID"].value_counts(ascending=False))

##plot
#df["LojaID"].value_counts(ascending=False).plot.bar()

##barras horizontais
#df["LojaID"].value_counts(ascending=True).plot.barh()

##plot pizza
#df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

##total vendas por cidade
#print(df["Cidade"].value_counts())

##nome aos eixos
#df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color="red")
#plt.xlabel("Cidade")
#plt.ylabel("Total vendas")

##legenda
#plt.style.use("ggplot")
#df.groupby(df["mesVenda"])["Qtde"].sum().plot(title="Total produtos vendidos x mês")
#plt.xlabel("Mês")
#plt.ylabel("Total produtos vendidos")
#plt.legend()

##
#df.groupby(df["mesVenda"])["Qtde"].sum()
# df2019 = df[df["Data"].dt.year == 2019]
# df2019.groupby(df2019["Data"].dt.month)["Qtde"].sum().plot(marker="o")
# plt.xlabel("produtos vendidos")
# plt.ylabel("Mês")
# plt.legend()
# plt.show();

##histograma
#plt.hist(df["Qtde"], color="magenta")
#plt.show()

#scatter
df2019 = df[df["Data"].dt.year == 2019]
plt.scatter(x = df2019["Data"].dt.day, y = df2019["Receita"])
plt.savefig("grafico.png")