from itertools import permutations
n = int(input())
nums = list(map(int, input().split()))
cases = list(permutations(nums))
result = []
for case in cases:
    sum = 0
    for i in range(0,n-1):
        sum = sum + abs(case[i] - case[i+1])
    result.append(sum)
print(max(result))