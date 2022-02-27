from sys import stdin
from collections import deque
INF = 987654321
input = stdin.readline

N, K = map(int, input().split())

def bfs(start, end):
    space = [INF] * 100001
    space[start] = 0
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        if x * 2 >= 0 and x * 2 <= 100000:
            if space[x] < space[x * 2]:
                space[x * 2] = space[x]
                queue.append(x * 2)
        if x - 1 >= 0:
            if space[x] + 1 < space[x - 1]:
                space[x - 1] = space[x] + 1
                queue.append(x - 1)
        if x + 1 <= 100000:
            if space[x] + 1 < space[x + 1]:
                space[x + 1] = space[x] + 1
                queue.append(x + 1)
        if x + 1 == end or x - 1 == end or x * 2 == end:
            break
    return space[end]

print(bfs(N, K))
