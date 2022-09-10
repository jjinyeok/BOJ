from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    queue = deque()
    queue.append(1)
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if parent[i] == 0:
                parent[i] = node
                queue.append(i)

bfs()
for i in parent[2:]:
    print(i)
