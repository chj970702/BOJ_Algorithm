import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

result = [-1] * n
stack = []

for i in range(n):
    while stack and li[stack[-1]] < li[i]:
        result[stack.pop()] = li[i]
    stack.append(i)

for item in result:
    sys.stdout.write(str(item) + ' ')

# import sys
# n = int(sys.stdin.readline())
# li = list(map(int, sys.stdin.readline().split()))
#
# result = [-1] * n
# for i in range(n):
#     for j in range(i+1, n):
#         if li[j] > li[i]:
#             result[i] = li[j]
#             break
# for item in result:
#     sys.stdout.write(str(item) + ' ')
# nge = [[]for i in range(n)]
# for i in range(n):
#     for j in range(i+1, n):
#         if li[j] > li[i]:
#             nge[i].append(li[j])
#
# result = []
# for i in range(n):
#     if len(nge[i]) == 0:
#         result.append(-1)
#     else:
#         result.append(nge[i][0])
# for item in result:
#     sys.stdout.write(str(item) + ' ')