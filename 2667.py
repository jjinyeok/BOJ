from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().rstrip())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
results = []
def bfs(start):
    queue = deque()
    queue.append(start)
    count = 1
    arr[start[0]][start[1]] = 2
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >=0 and nx <= N - 1 and ny <= N - 1:
                if arr[nx][ny] == 1:
                    queue.append([nx, ny])
                    arr[nx][ny] = 2
                    count += 1
    results.append(count)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bfs([i, j])

print(len(results))
results.sort()
print('\n'.join(map(str, results)))
