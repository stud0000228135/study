def compress():
    word = input('Введите последовательность: ')
    count = 1
    compressed = ''
    for letter in range (1, len(word)):
        if word[letter] == word[letter-1]:
            count += 1
        else:
            compressed += word[letter-1]
            compressed += str(count)
            count = 1
    else:
        compressed += word[letter]
        compressed += str(count)
        count = 1
    print(compressed)

compress()