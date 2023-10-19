from itertools import permutations
k = int(input())
li = list(input().split())
nums = set()
for i in range(10):
    nums.add(i)
cases = permutations(nums, k+1)
result = []
for case in cases:
    valid = True
    for i in range(k):
        if li[i] == ">":
            if case[i] <= case[i+1]:
                valid = False
                break
        else:
            if case[i] >= case[i+1]:
                valid = False
                break
    if (valid):
        result.append(case)
for item in max(result):
    print(item, end="")
print()
for item in min(result):
    print(item, end="")