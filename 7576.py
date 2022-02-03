from collections import deque
from sys import stdin
M, N = map(int, stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(map(int, stdin.readline().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i, j])

result = 0
while queue:
    tmp_pop = []
    while queue:
        tmp_pop.append(queue.popleft())
    for [x, y] in tmp_pop:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx <= N - 1 and ny <= M - 1:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    queue.append([nx, ny])
    result += 1

answer = True
for i in range(N):
    if 0 in arr[i]:
        answer = False        
        break

if answer:
    print(result - 1)
else:
    print(-1)