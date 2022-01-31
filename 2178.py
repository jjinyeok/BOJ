from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
maze = []
for i in range(N):
    maze.append(list(map(int, stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] += maze[x][y]
                queue.append((nx, ny))

bfs(0, 0)
print(maze[N - 1][M - 1])