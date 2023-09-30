x = int(input())
num_prev = 0
num_cur = 1
num_x = 0
if x == 0:
    print(0)
else:
    for i in range(0, x - 1):
        num_x = num_prev + num_cur
        num_prev = num_cur
        num_cur = num_x
    print(num_x)
