import re


def check_password(password):
    if not re.search(r'[a-z]', password):
        return False
    elif not re.search(r'\d', password):
        return False
    elif not re.search(r'[A-Z]', password):
        return False
    elif not re.search(r'[\W_]', password):
        return False
    elif len(password) < 6:
        return False
    elif len(password) > 12:
        return False
    else:
        return True


input_password = input("Введите пароль: ")
if check_password(input_password):
    print(check_password(input_password))
else:
    print(not check_password(input_password))
