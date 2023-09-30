x = input()
num = 0

while len(x) > 1:
    for i in x:
        num += int(i)
    else:
        x = str(num)
        num = 0

print (x)

