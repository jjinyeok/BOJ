from sys import stdin
from collections import deque
m, n, h = map(int, stdin.readline().split())
xyz = []
for _ in range(h):
    xy = []
    for _ in range(n):
        xy.append(list(map(int, stdin.readline().split())))
    xyz.append(xy)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()

for i in range(h):
        for j in range(n):
            for k in range(m):
                if xyz[i][j][k] == 1:
                    q.append([i, j, k])

count = 0
while q:
    x, y, z = q.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if nx >= 0 and nx <= h - 1 and ny >= 0 and ny <= n - 1 and nz >= 0 and nz <= m - 1:
            if xyz[nx][ny][nz] == 0:
                xyz[nx][ny][nz] = xyz[x][y][z] + 1
                q.append([nx, ny, nz])

count = 0
ripe_no = False
for i in range(h):
        for j in range(n):
            for k in range(m):
                if xyz[i][j][k] > count:
                    count = xyz[i][j][k]
                if xyz[i][j][k] == 0:
                    ripe_no = True

if ripe_no:
    print(-1)
else:
    print(count - 1)
