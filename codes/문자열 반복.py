n = int(input())
li = []
for i in range(n):
    li.append(list(input().split()))
result = []
for item in li:
    new_str = ''
    for i in range(len(item[1])):
        for j in range(int(item[0])):
            new_str = new_str + str(item[1][i])
    result.append(new_str)
for item in result:
    print(item)