f = open("data.csv")
for line in f:
    data = line.split(",")
    name = data[3][1:] + data[4][:-1]
    if data[6] == "":
        age = "Unknown"
    else:
        age = data[6]
    ti_class = data[2]
    sex = data[5].capitalize()
    if data[2] == "1":
        survived = "Survived"
    else:
        survived = "Not Survived"
    if name == "ameSe":
        continue
    else:
        print(f"{name:55}{age:11}{ti_class:5}{sex:10}{survived:16}")
f.close()
