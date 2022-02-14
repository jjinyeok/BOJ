from copy import deepcopy
from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split())
space = []
for i in range(N):
    space.append(list(map(int, input().split())))

zeros = []
for i in range(N):
    for j in range(M):
        if space[i][j] == 0:
            zeros.append([i, j])

virus = []
for i in range(N):
    for j in range(M):
        if space[i][j] == 2:
            virus.append([i, j])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(starts, arr):
    queue = deque()
    for start in starts:
        queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx <= N - 1 and ny <= M - 1:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    queue.append([nx, ny])
    return arr

result = 0
for i in range(len(zeros) - 2):
    for j in range(i + 1, len(zeros) - 1):
        for k in range(j + 1, len(zeros)):
            new_space = deepcopy(space)
            x1, y1 = zeros[i]
            x2, y2 = zeros[j]
            x3, y3 = zeros[k]
            new_space[x1][y1] = 1
            new_space[x2][y2] = 1
            new_space[x3][y3] = 1
            result_space = bfs(virus, new_space)
            count = 0
            for a in range(N):
                for b in range(M):
                    if result_space[a][b] == 0:
                        count += 1
            if count > result:
                result = count

print(result)
