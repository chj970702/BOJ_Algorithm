n = int(input())
li = []
same = [0] * n
for i in range(n):
    li.append(list(map(int, input().split())))
    same[i] = [0] * n
for i in range(5): # 학년
    for j in range(n): #j번 학생의 i 학년
        for k in range(j+1, n):
            if li[j][i] == li[k][i]: # j번과 k번이 i학년때 같은반
                same[j][k] = 1
                same[k][j] = 1

cnt = [0] * n
for i in range(n):
    number = same[i].count(1)
    cnt[i] = number
max = max(cnt)
print(cnt.index(max)+1)