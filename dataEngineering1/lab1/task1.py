f = open("data.csv")
count_survived = 0
for line in f:
    data = line.split(",")
    if data[1] == "1":
        count_survived += 1
    else:
        continue
f.close()

print(f"Количество спасенных пассажиров: ", count_survived)
