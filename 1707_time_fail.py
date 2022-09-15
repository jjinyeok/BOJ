import sys
from collections import deque

# input
k = int(sys.stdin.readline())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = {i: [] for i in range(1, v + 1)}
    case = []
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        case.append([a, b])
        graph[a].append(b)
        graph[b].append(a)

    for a, b in case:
        visited = [0 for _ in range(v + 1)]
        success = True
        q_1 = deque([a])
        visited[a] = 1
        while q_1:
            temp_a = q_1.popleft()
            for i in graph[temp_a]:
                if visited[i] == 0 and i != b:
                    q_1.append(i)
                    visited[i] = 1
        q_2 = deque([b])
        visited[b] = 2
        while q_2:
            temp_b = q_2.popleft()
            for i in graph[temp_b]:
                if visited[i] == 0:
                    q_2.append(i)
                    visited[i] = 2
                if visited[i] == 1 and i != a:
                    success = False
    
    if success:
        print('YES')
    else:
        print('NO')