n = int(input())
cnt = 0
og = n
while True:
    first = n // 10
    second = n % 10
    third = first + second
    new = 10 * second + (third % 10)
    cnt += 1
    if new == og:
        break
    else:
        n = new
print(cnt)
