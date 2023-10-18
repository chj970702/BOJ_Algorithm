c = int(input())
for i in range(0, c):
    li = list(map(int, input().split()))
    avg = (sum(li)-li[0]) / li[0]
    cnt = 0
    for j in range(1,li[0]+1):
        if li[j] > avg:
            cnt = cnt +1
    print("%.3f" % (cnt / li[0] * 100)+"%")