from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    if b not in arr[a]:
        arr[a].append(b)
    if a not in arr[b]:
        arr[b].append(a)

result = [101] * (N + 1)
def bfs(start):
    queue = deque()
    num = [0] * (N + 1)
    visited = [False for _ in range(N + 1)]
    visited[start] = True
    queue.append(start)
    while queue:
        now = queue.popleft()
        for i in arr[now]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                num[i] = num[now] + 1
    tmp = sum(num)
    result[start] = tmp

for i in range(1, N + 1):
    bfs(i)
print(result.index(min(result)))
