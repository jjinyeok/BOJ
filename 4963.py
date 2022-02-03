from sys import stdin
from collections import deque

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
def bfs(arr, start, height, width):
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx <= height - 1 and ny <= width - 1:
                if arr[nx][ny] == 1:
                    queue.append([nx, ny])
                    arr[nx][ny] = 0
    
while True:
    W, H = map(int, stdin.readline().split())
    if W == 0 and H == 0:
        break
    arr = []
    result = 0
    for i in range(H):
        arr.append(list(map(int, stdin.readline().split())))
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1:
                bfs(arr, [i, j], H, W)
                result += 1
    print(result)