import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
graph = [[-1 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    graph[r - 1][c - 1] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answers = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            area = 1
            graph[i][j] = 1
            q = deque([[i, j]])
            while q:
                y, x = q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if ny >= 0 and ny <= n - 1 and nx >= 0 and nx <= m - 1 and graph[ny][nx] == 0:
                        graph[ny][nx] = 1
                        area += 1
                        q.append([ny, nx])
            answers.append(area)

print(max(answers))
