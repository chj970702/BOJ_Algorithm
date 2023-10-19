import sys
n,m = map(int, input().split())
from itertools import permutations

nums = []
for i in range(n):
    nums.append(i+1)

cases = list(permutations(nums,m))
length = len(cases)
for idx, case in enumerate(cases):
    for item in case:
        sys.stdout.write(str(item) + " ")
    if idx != length - 1:
        sys.stdout.write("\n")
