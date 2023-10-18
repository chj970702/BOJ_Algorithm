import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    key = sys.stdin.readline()
    if "push" in key:
        word, num = key.split()
        stack.append(num)
    elif "pop" in key:
        if len(stack) == 0:
            sys.stdout.write(str(-1)+"\n")
        else:
            last = stack.pop()
            sys.stdout.write(str(last)+"\n")
    elif "size" in key:
        sys.stdout.write(str(len(stack))+"\n")
    elif "empty" in key:
        if len(stack) == 0:
            sys.stdout.write(str(1)+"\n")
        else:
            sys.stdout.write(str(0)+"\n")
    else:
        if len(stack) == 0:
            sys.stdout.write(str(-1)+"\n")
        else:
            sys.stdout.write(str(stack[-1])+"\n")