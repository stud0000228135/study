x = input()
x = x.lower()
ABC = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
num = "0123456789"
letters = 0
digits = 0
symbols = 0
for i in x:
    if i in ABC:
        letters += 1
    elif i in num:
        digits += 1
    else:
        symbols += 1

print(letters, digits, symbols, sep='\n')
