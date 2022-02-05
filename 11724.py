from sys import stdin
from collections import deque

input = stdin.readline
N, M = map(int, input().split())

visited = [False] * (N + 1)
visited[0] = True

arr = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

result = []
def bfs(start):
    queue = deque()
    if visited[start] == False:
        result.append(1)
    queue.append(start)
    while queue:
        x = queue.popleft()
        for i in arr[x]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

for i in range(1, N + 1):
    bfs(i)

print(result.count(1))