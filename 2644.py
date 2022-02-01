from sys import stdin
from collections import deque
N = int(stdin.readline())
start, end = map(int, stdin.readline().split())
M = int(stdin.readline())
graph = []
for i in range(M):
    parent, child = map(int, stdin.readline().split())
    graph.append([parent, child])
    graph.append([child, parent])

graph.sort()
visited = [-1] * (N + 1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:
        x = queue.popleft()
        for i in range(M * 2):
            if graph[i][0] == x and visited[graph[i][1]] == -1:
                queue.append(graph[i][1])
                visited[graph[i][1]] = visited[x] + 1
    return -1

bfs(start)
print(visited[end])