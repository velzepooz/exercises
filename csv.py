import csv


rows = []
with open("m5-buckwheat.csv") as fp:
    reader = csv.reader(fp)
    for row in reader:
        rows.append(row)
fields = rows[0]
rows = rows[1:]
print(fields)
print(rows)

# максимальная цена манки
# m = 0
# for r in rows:
#     val = float(r[1])
#     if val > m:
#         m = val
# print(m)

m = 40.71
for r in rows:
    val = float(r[1])
    if val < m:
        m = val
print(m * 0.250)
