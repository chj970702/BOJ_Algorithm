a, b = map(int, input().split())
li = []
for i in range(1, 1000):
    cnt = i
    while cnt != 0:
        li.append(i)
        cnt = cnt - 1
nums = li[a-1:b]
print(sum(nums))