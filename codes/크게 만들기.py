n,k = map(int, input().split())
num = input()
stack = []
for item in num:
    while stack and stack[-1] < item and k>0:
        stack.pop()
        k = k-1
    stack.append(item)
if k>0:
    stack = stack[:-k]
    for item in stack:
        print(item,end='')
else:
    for item in stack:
        print(item,end='')