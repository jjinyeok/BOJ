import queue
from sys import stdin
from collections import deque
N = int(stdin.readline())
arr = []
for i in range(N):
    arr.append(list(stdin.readline().rstrip()))

unnormal_arr = []
for i in range(N):
    tmp_arr = []
    for j in range(N):
        if arr[i][j] == 'G':
            tmp_arr.append('R')
        else:
            tmp_arr.append(arr[i][j])
    unnormal_arr.append(tmp_arr)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(arr, start, color):
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx <= N - 1 and ny <= N - 1:
                if arr[nx][ny] == color:
                    arr[nx][ny] = '0'
                    queue.append([nx, ny])

result = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            bfs(arr, [i, j], 'R')
            result += 1
        if arr[i][j] == 'B':
            bfs(arr, [i, j], 'B')
            result += 1
        if arr[i][j] == 'G':
            bfs(arr, [i, j], 'G')
            result += 1

unnormal_result = 0
for i in range(N):
    for j in range(N):
        if unnormal_arr[i][j] == 'R':
            bfs(unnormal_arr, [i, j], 'R')
            unnormal_result += 1
        if unnormal_arr[i][j] == 'B':
            bfs(unnormal_arr, [i, j], 'B')
            unnormal_result += 1

print(result, unnormal_result)
