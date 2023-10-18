from collections import deque

N, K = map(int, input().split())

# 방문 여부와 시간을 저장하는 배열
visited = [-1] * 100001
visited[N] = 0

queue = deque([N])

while queue:
    current = queue.popleft()

    # 현재 위치에서 이동할 수 있는 3가지 위치
    for next_pos in [current - 1, current + 1, current * 2]:
        # 유효한 위치이고 아직 방문하지 않았다면
        if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
            visited[next_pos] = visited[current] + 1
            queue.append(next_pos)
            # 만약 동생의 위치를 찾았다면, 반복문 종료
            if next_pos == K:
                break

print(visited[K])
