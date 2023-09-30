def find_anagrams():
    words = input('Введите слова: ').lower()
    words = words.split()
    anagram_pairs = {}

    for word in words:
        sorted_letters = ''.join(sorted(word))
        if sorted_letters not in anagram_pairs:
            anagram_pairs[sorted_letters] = [word]
        else:
            anagram_pairs[sorted_letters].append(word)
            anagram_pairs[sorted_letters].sort()

    mess = sorted(anagram_pairs.values())

    for items in mess:
        if len(items) > 1:
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    print(items[i], items[j])


find_anagrams()
