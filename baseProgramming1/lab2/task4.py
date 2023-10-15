def find_anagrams():
    words = input('Введите слова: ').lower()
    words = words.split()
    anagram_pairs = {}

    for word in words:
        sorted_letters = ''.join(sorted(word))
        if sorted_letters not in anagram_pairs:
            anagram_pairs[sorted_letters] = [word]
        elif word in anagram_pairs.get(sorted_letters):
            continue
        else:
            anagram_pairs[sorted_letters].append(word)
            anagram_pairs[sorted_letters].sort()

    mess = sorted(anagram_pairs.values())

    for items in mess:
        if len(items) > 1:
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    if items[i] != items[j]:
                        print(items[i], items[j])
                    else:
                        continue


find_anagrams()
