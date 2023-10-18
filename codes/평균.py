n = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)
for i in range(len(score_list)):
    score_list[i] = score_list[i] / max_score * 100
total = sum(score_list)
avg = total / len(score_list)
print(avg)