# import sys
# n = int(sys.stdin.readline())
# li = []
# for i in range(n):
#     num = int(sys.stdin.readline())
#     li.append(num)
# li.sort()
# for i in li:
#     sys.stdout.write(str(i)+ "\n")
import sys
n = int(sys.stdin.readline())
count = [0] * 10001
for i in range(n):
    num = int(sys.stdin.readline())
    count[num] = count[num] + 1

for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):
            sys.stdout.write(str(i) +"\n")