import sys
from collections import deque

n = int(sys.stdin.readline())
graph = {i: [] for i in range(n)}
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if row[j] == 1:
            graph[i].append(j)

for i in range(n):
    q = deque(graph[i])
    while q:
        node = q.popleft()
        for element in graph[node]:
            if element not in graph[i]:
                graph[i].append(element)
                q.append(element)

answer = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j in graph[i]:
            answer[i][j] = 1
for row in answer:
    print(' '.join(map(str, row)))
