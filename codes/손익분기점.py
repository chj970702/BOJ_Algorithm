import sys
a, b, c = map(int, sys.stdin.readline().split())
num = 1
if b >= c:
    sys.stdout.write(str(-1))
else:
    sys.stdout.write(str(a // (c-b) + 1))