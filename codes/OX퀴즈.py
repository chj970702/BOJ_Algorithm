n = int(input())
li = []
score = []
for i in range(n):
    new_list = list(input())
    li.append(new_list)
    score.append([0] * (len(new_list) + 1))
for i in range(n):
    for j in range(len(li[i])):
        if li[i][j] == 'O':
            score[i][j+1] = score[i][j] + 1
for item in score:
    print(sum(item))
