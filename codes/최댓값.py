li = []
for i in range(9):
    li.append(int(input()))
k = max(li)
idx = li.index(k)
print(max(li), idx+1)