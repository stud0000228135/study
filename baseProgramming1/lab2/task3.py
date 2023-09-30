def unique():
    not_unique = str(input('Введите последовательность: ')).lower()
    not_unique = not_unique.split()

    temp_list = []
    for i in not_unique:
        if i not in temp_list:
            temp_list.append(i)

    unique = temp_list

    print(*unique)

unique()