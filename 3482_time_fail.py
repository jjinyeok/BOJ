import sys
from collections import deque

# input
n = int(sys.stdin.readline())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(y):
        graph.append(list(sys.stdin.readline().strip()))

# make case (blind alley)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    case = []
    for i in range(y):
        for j in range(x):
            if graph[i][j] == '.':
                count = 0
                for k in range(4):
                    if graph[i + dy[k]][j + dx[k]] == '#':
                        count += 1
                if count == 3:
                    case.append([i, j])

    answer = 0
    for a, b in case:
        copy_graph = [item[:] for item in graph]
        q = deque([[a, b]])
        copy_graph[a][b] = 0
        while q:
            ny, nx = q.popleft()
            for k in range(4):
                if copy_graph[ny + dy[k]][nx + dx[k]] == '.':
                    q.append([ny + dy[k], nx + dx[k]])
                    copy_graph[ny + dy[k]][nx + dx[k]] = copy_graph[ny][nx] + 1
                    if copy_graph[ny][nx] + 1 > answer:
                        answer = copy_graph[ny][nx] + 1
    print(f'Maximum rope length is {answer}.')
