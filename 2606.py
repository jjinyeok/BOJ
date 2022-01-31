from sys import stdin
from collections import deque

N = int(stdin.readline())
connection = int(stdin.readline())
graph = [[]for _ in range(N + 1)]
graph.append([])
for i in range(connection):
    x, y = (map(int, stdin.readline().split()))
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N + 1)
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    result = 0
    current = start
    while queue:
        current = queue.popleft()
        #print(current, end=' ')
        for i in graph[current]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                result += 1
    return result

print(bfs(1))