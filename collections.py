from collections import Counter


# Digits
data = [2, 4, 2, 2, 4, 6, 2, 4, 6, 7, 15, 2, 8]
c = Counter(data)
print(c.most_common())
print("Two most common entries:")
for entry, count in c.most_common(2):
    print(f" {entry} (met {count} times)")

# str
data = "aosneuhaoseuahonusaohuno"
c = Counter(data)
print(c.most_common())
print("Two most common entries:")
for entry, count in c.most_common(2):
    print(f" {entry} (met {count} times)")

""" Счетчик можно обновлять, внося в него новые данные. """
c = Counter()
c.update("aosn euhaoseuahonusaohuno")
c.update("aaaaaaaaaaaaaa")
print(c.most_common(3))
