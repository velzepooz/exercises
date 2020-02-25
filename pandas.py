import pandas
data = pandas.read_csv("m5-buckwheat.csv")
# print(data)

# s = data["Крупа манная, кг"]
# print(s)

# s = data[0:5]["Крупа манная, кг"] # первые пять элментов колонки
# print(s)

# s = data[["Крупа манная, кг", "Год"]]
# print(s)

s = data["Крупа манная, кг"]
s.min()
s.max()
s.median()
print(s.mean())
