import heapq
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

starts = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            starts.append([0, graph[i][j], i, j]) #second, kindOfVirus, x, y

def bfs(starts, time):
    q = []
    for start in starts:
        heapq.heappush(q, start)
    while q:
        second, virus, x, y = heapq.heappop(q)
        if second >= time:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx <= N - 1 and ny <= N - 1:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]
                    heapq.heappush(q, [second + 1, graph[nx][ny], nx, ny])

bfs(starts, S)
print(graph[X - 1][Y - 1])
