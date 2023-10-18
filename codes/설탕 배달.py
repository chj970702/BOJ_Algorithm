n = int(input())
count_5 = n // 5
while count_5 >= 0:
    rest = n - 5 * count_5
    if rest % 3 == 0:
        count_3 = rest // 3
        break
    else:
        count_5 = count_5 - 1

if (count_5 < 0 ):
    print(-1)
else:
    print(count_5 + count_3)
