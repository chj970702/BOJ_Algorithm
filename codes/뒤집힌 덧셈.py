def rev(x):
    x_list = list(x)
    x_list.reverse()
    idx = 0
    num = 0
    for i in x_list:
        num = num + int(i) * 10 ** (len(x_list) - idx - 1)
        idx = idx + 1
    return num
x, y = input().split()

print(rev(str(rev(x)+rev(y))))