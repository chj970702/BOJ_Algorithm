n = int(input())
k = 1
li = []
while k<n:
    li.append(k * (n+1))
    k = k+1
print(sum(li))