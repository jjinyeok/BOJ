import sys
from collections import deque

# input
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    input_list = list(map(int, sys.stdin.readline().split()))
    graph = {i: [] for i in range(1, n + 1)}
    visited = [False for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i].append(input_list[i - 1])
        graph[input_list[i - 1]].append(i)

# solution by bfs
    answer = 0
    for i in range(1, n + 1):
        if visited[i] == False:
            q = deque([i])
            answer += 1
            while q:
                now = q.popleft()
                for j in graph[now]:
                    if visited[j] == False:
                        q.append(j)
                        visited[j] = True
    print(answer)
