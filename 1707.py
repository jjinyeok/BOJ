import sys
from collections import deque

# input
k = int(sys.stdin.readline())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    connection = [[] for _ in range(v + 1)]
    graph = [0 for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        connection[a].append(b)
        connection[b].append(a)

# find answer
    answer = 'YES'
    for i in range(1, v + 1):
        if answer == 'NO':
            break
        if graph[i] == 0:
            graph[i] = 1
            q = deque([i])
            while q:
                if answer == 'NO':
                    break
                now = q.popleft()
                for child in connection[now]:
                    if graph[child] == 0:
                        graph[child] = graph[now] * (-1)
                        q.append(child)
                    elif graph[child] == graph[now]:
                        answer = 'NO'

# output
    print(answer)
