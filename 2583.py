import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x_1, y_1, x_2, y_2 = map(int, sys.stdin.readline().split())
    for y in range(m - y_2, m - y_1):
        for x in range(x_1, x_2):
            graph[y][x] = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            area = 1
            graph[i][j] = 1
            q = deque()
            q.append([i, j])
            while q:
                y, x = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if ny >= 0 and ny <= m - 1 and nx >= 0 and nx <= n - 1 and graph[ny][nx] == 0:
                        graph[ny][nx] = 1
                        area += 1
                        q.append([ny, nx])
            answer.append(area)

answer.sort()
print(len(answer))
print(' '.join(map(str, answer)))
