import sys
from collections import deque

# input
n, m, v = map(int, sys.stdin.readline().split())
graph = {}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a in graph: graph[a].append(b)
    else: graph[a] = [b]
    if b in graph: graph[b].append(a)
    else: graph[b] = [a]
for key, value in graph.items():
    value.sort()

# dfs
dfs_answer = [v]
dfs_visited = [False for _ in range(n + 1)]
dfs_visited[v] = True
stack = deque([v])
while stack:
    now = stack[len(stack) - 1]
    check = True
    if now in graph:
        for i in graph[now]:
            if dfs_visited[i] == False:
                stack.append(i)
                dfs_answer.append(i)
                dfs_visited[i] = True
                check = False
                break
    if check:
        stack.pop()

# bfs
bfs_answer = [v]
bfs_visited = [False for _ in range(n + 1)]
bfs_visited[v] = True
queue = deque([v])
while queue:
    now = queue.popleft()
    if now in graph:
        for i in graph[now]:
            if bfs_visited[i] == False:
                queue.append(i)
                bfs_answer.append(i)
                bfs_visited[i] = True

print(' '.join(map(str, dfs_answer)))
print(' '.join(map(str, bfs_answer)))
