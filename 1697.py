from sys import stdin
from collections import deque
input = stdin.readline

N, K = map(int, input().split())
arr = [-1] * 100001

def bfs(start):
    queue = deque()
    queue.append(start)
    arr[start] = 0
    while queue:
        x = queue.popleft()
        if x + 1 <= 100000 and arr[x + 1] == -1:
            arr[x + 1] = arr[x] + 1
            queue.append(x + 1)
        if x - 1 >= 0 and arr[x - 1] == -1:
            arr[x - 1] = arr[x] + 1
            queue.append(x - 1)
        if x * 2 <= 100000 and arr[x * 2] == -1:
            arr[x * 2] = arr[x] + 1
            queue.append(x * 2)

bfs(N)
print(arr[K])