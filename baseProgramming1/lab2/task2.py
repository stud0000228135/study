abc = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def stat():
    word = input('Введите последовательность: ').lower()
    count = 0
    new_word = []
    for i in range(len(word)):
        for j in range(len(word)):
            if word[i] == word[j]:
                count += 1
        else:
            for_new_word = [word[i], count]
            new_word.append(for_new_word)
            count = 0

    new_word = sorted(new_word, key=lambda letter: letter[0])

    temp_list = []
    for i in new_word:
        if i not in temp_list:
            temp_list.append(i)

    new_word = temp_list

    for i in range(len(new_word)):
        if new_word[i][0] in abc:
            print(new_word[i][0], new_word[i][1])


stat()
