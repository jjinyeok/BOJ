from sys import stdin
from collections import deque
input = stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(arr, start, N):
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx <= N - 1 and ny <= N - 1:
                if arr[nx][ny] == 0:
                    queue.append([nx, ny])
                    arr[nx][ny] = arr[x][y] + 1

T = int(input())
for i in range(T):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    bfs(arr, [start_x, start_y], N)
    if start_x == end_x and start_y == end_y:
        print(0)
    else:
        print(arr[end_x][end_y])