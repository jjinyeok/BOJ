import sys
from collections import deque

while True:
    l, r, c = map(int, sys.stdin.readline().split())
    if l == 0 and r == 0 and c == 0:
        break

    graph_3d = []
    for layer_num in range(l):
        graph_2d = []
        for row_num in range(r):
            row = list(sys.stdin.readline().strip())
            if 'S' in row:
                start = [layer_num, row_num, row.index('S')]
            if 'E' in row:
                end = [layer_num, row_num, row.index('E')]
            graph_2d.append(row)
        sys.stdin.readline()
        graph_3d.append(graph_2d)

    answer = 'Trapped!'
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    q = deque([start])
    graph_3d[start[0]][start[1]][start[2]] = 0
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx <= l - 1 and 0 <= ny <= r - 1 and 0 <= nz <= c - 1:
                if graph_3d[nx][ny][nz] == '.':
                    graph_3d[nx][ny][nz] = graph_3d[x][y][z] + 1
                    q.append([nx, ny, nz])
                if graph_3d[nx][ny][nz] == 'E':
                    answer = f'Escaped in {graph_3d[x][y][z] + 1} minute(s).'
    print(answer)
