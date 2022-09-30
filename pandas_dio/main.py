import pandas as pd

df = pd.read_csv("C:/Users/BlueShift/PycharmProjects/pandas_dio/datasets/Gapminder.csv", on_bad_lines='skip', sep=";")

print(df)

#df = df.rename(columns = {"country":"pais", "continent": "continente", "year":"ano", "lifeExp":"expectativa de vida",
                     #"pop":"Pop total","gdpPercap":"PIB"})

#print(df.head(10))

#print(df.shape)

#print(df.columns)

#print(df.dtypes)

#print(df.tail(15))

#print(df.describe())

#print(df["continente"].unique())

#oceania = df.loc[df["continente"] == "Oceania"]
#print(oceania.head())

#print(df.groupby("continente")["pais"].nunique())
#print(df.groupby("ano")["expectativa de vida"].mean())

#print(df["PIB"].sum())