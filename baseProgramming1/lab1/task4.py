x = int(input())

if x % 10 == 1 and x % 100 != 11:
    print("комментарий")
elif 2 <= x % 10 <= 4 and (x % 100 < 10 or x % 100 >= 20):
    print("комментария")
else:
    print("комментариев")
    
"""0 комментариев
1 комментарий
2 комментария
3 комментария
4 комментария
5 комментариев
6 комментариев
7 комментариев
8 комментариев
9 комментариев
10-20 комментариев"""