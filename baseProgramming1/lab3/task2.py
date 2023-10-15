import re

words = input('Введите слова: ').split()
num = list(input('Введите числа: '))

dict_words = {}

for word in words:
    dict_words[word] = []
    for letter in word:
        if re.findall(r'[а-г]', letter, re.I):
            dict_words[word].append('2')
        elif re.findall(r'[д-зё]', letter, re.I):
            dict_words[word].append('3')
        elif re.findall(r'[и-л]', letter, re.I):
            dict_words[word].append('4')
        elif re.findall(r'[м-п]', letter, re.I):
            dict_words[word].append('5')
        elif re.findall(r'[р-у]', letter, re.I):
            dict_words[word].append('6')
        elif re.findall(r'[ф-ч]', letter, re.I):
            dict_words[word].append('7')
        elif re.findall(r'[ш-ы]', letter, re.I):
            dict_words[word].append('8')
        elif re.findall(r'[ь-я]', letter, re.I):
            dict_words[word].append('9')

result = []
for key in dict_words:
    if dict_words[key][0:len(num)] == num:
        result.append(key)

print(*result)
