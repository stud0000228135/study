x = input()
x = x.lower()
list1 = []
for i in x:
    y = x.count(i)
    list1.append(y)
z = max(list1)
a = list1.index(z)
print(x[a].upper())
