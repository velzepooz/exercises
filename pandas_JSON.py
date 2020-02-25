import pandas


data = pandas.read_json("m5-access-log-100.json")
s = data[-20:]["ip"]
print(s)

import pandas
data = pandas.read_json("m5-access-log-100.json")
print(data["ip"].value_counts()) #Это выведет нам информацию о том, как часто какой ip встречался в выборке.
