n, m = map(int, input().split())
li = []
for i in range(n):
    li.append(input())
cnt = 0
for i in range(n):
    if 'X' not in li[i]:
        cnt = cnt +1

cnt_2 = 0
for i in range(m):
    flag = True
    for j in range(n):
        if li[j][i] == 'X':
            flag = False
    if flag:
        cnt_2 = cnt_2 + 1
print(max(cnt, cnt_2))
