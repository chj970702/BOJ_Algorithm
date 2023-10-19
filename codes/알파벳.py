r,c = map(int, input().split())
li = []
for i in range(r):
    li.append(list(input()))
ans = 0
visited = set()
dx, dy = [-1,1,0,0], [0,0,-1,1]
def dfs(x,y,cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and li[nx][ny] not in visited:
            visited.add(li[nx][ny])
            dfs(nx, ny, cnt+1)
            visited.remove(li[nx][ny])

visited.add(li[0][0])
dfs(0,0, 1)
print(ans)