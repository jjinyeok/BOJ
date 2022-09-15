from sys import stdin
from collections import deque

# input
n, m = map(int, stdin.readline().split())
visited = [False] * (n + 1)
arr = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

# bfs : for finding connecting elements
def bfs(start):
    result = False
    queue = deque()
    if visited[start] == False:
        result = True
    queue.append(start)
    while queue:
        x = queue.popleft()
        for i in arr[x]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
    return result

# running full node bfs
answer = 0
for i in range(1, n + 1):
    if bfs(i):
        answer += 1

# output
print(answer)
