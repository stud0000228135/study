with open('requirement.txt', encoding='utf-8') as f:
    dirty = f.read().replace('->', '')
    dirty = dirty.replace('(', '')
    dirty = dirty.replace(')', '')
    dirty = dirty.replace('не пишется', 'нет')
    dirty = dirty.split()

clean = {}

rus = 0
eng = 2
for i in dirty:
    if eng < len(dirty):
        clean[dirty[rus]] = dirty[eng]
        rus += 1
        eng += 1

clean[' '] = ' '
clean['ь'] = ''

def translit():
    full_name_rus = input('Введите имя: ')
    full_name_eng = str()
    for letter in full_name_rus:
        full_name_eng += clean[letter]
    print(full_name_eng)


translit()
