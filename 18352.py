from sys import stdin
from collections import deque
input = stdin.readline
INF = 987654321

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

def bfs(first):
    arr = [INF] * (N + 1)
    arr[first] = 0
    queue = deque()
    queue.append(first)
    while queue:
        start = queue.popleft()
        for destination in graph[start]:
            if arr[destination] > arr[start] + 1:
                arr[destination] = arr[start] + 1
                queue.append(destination)
    return arr

arr = bfs(X)
result = 0
for i in range(1, N + 1):
    if arr[i] == K:
        print(i)
        result += 1
if result == 0:
    print(-1)
