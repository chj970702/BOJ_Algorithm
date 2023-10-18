yundo = input()
n = int(input())
li = []
for _ in range(n):
    li.append(input())
li.sort()
yundo_l=yundo.count("L")
yundo_o=yundo.count("O")
yundo_v=yundo.count("V")
yundo_e=yundo.count("E")
result = []
for item in li:
    l = item.count("L") + yundo_l
    o = item.count("O") + yundo_o
    v = item.count("V") + yundo_v
    e = item.count("E") + yundo_e
    percent = ((l+o) * (l+v) * (l+e) * (o+v) * (o+e) * (v+e)) % 100
    result.append(percent)
idx = result.index(max(result))
print(li[idx])