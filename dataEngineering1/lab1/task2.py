f = open("data.csv")
count_survived_women = 0
sum_age = 0
for line in f:
    data = line.split(",")
    if data[1] == "1" and data[5] == "female":
        count_survived_women += 1
        if data[6] == '':
            continue
        sum_age += float(data[6])
    else:
        continue
f.close()

result = sum_age/count_survived_women
print(f"Средний возраст спасенных женщин: ", result)
