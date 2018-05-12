import pandas as pd
import matplotlib.pyplot as plt

url ="http://vincentarelbundock.github.io/Rdatasets/csv/datasets/HairEyeColor.csv"

data = pd.read_csv(url)
print(data)
print(type(data))

header = list(data)
print(header)

#print(data[['Unnamed: 0']])


print(data.shape)

print(data.dtypes)
ind = data.index
print(len(data.index))

#print(help(pd))
des = data.describe()
print(des)

x = data[['Unnamed: 0']]
y= data[["Freq"]]

plt.plot(x,y)
plt.show()

loc= data.iloc[0:3]
print(loc)

fil = data.query("Hair == 'Black'")
print(fil)

uni  =data["Eye"].unique()
print(uni)

data.d


col = data.groupby("Hair").agg({"Freq":"max"})
print(col)


