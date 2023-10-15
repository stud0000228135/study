import re

check_rgb1 = re.compile(r'rgb\((?:[0-2]?[0-9]?[0-9],?\s?){3}\)')
check_rgb2 = re.compile(r'rgb\((?:[0-9][0-9]?0?%,?\s?){3}\)')
check_rgb3 = re.compile(r'rgba\((?:[0-2][0-5]?[0-5]?,?\s?){3}[.,]\s?[0-1]*\)')


def check_rgb(rgb):
    if check_rgb1.match(rgb):
        return True
    elif check_rgb2.match(rgb):
        return True
    elif check_rgb3.match(rgb):
        return True
    else:
        return False


rgb_input = input()
print(check_rgb(rgb_input))
