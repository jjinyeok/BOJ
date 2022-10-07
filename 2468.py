import sys
from collections import deque

# input
n = int(sys.stdin.readline())
area = []
max_height = 0
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    if max_height < max(row): max_height = max(row)
    area.append(row)

# bfs
def bfs(area, n):
    count = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(n):
            if area[i][j] == False:
                count += 1
                q = deque([[i, j]])
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx >= 0 and nx <= n - 1 and ny >= 0 and ny <= n -1 and area[nx][ny] == False:
                            q.append([nx, ny])
                            area[nx][ny] = True
    return count

# find answer
answer = 0
for val in range(0, max_height + 1):
    new_area = [[True] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] <= val:
                new_area[i][j] = True
            else: 
                new_area[i][j] = False
    count = bfs(new_area, n)
    if answer < count:
        answer = count

print(answer)
