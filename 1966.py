import queue
from sys import stdin
from collections import deque
T = int(stdin.readline())
for i in range(T):
    N, M = map(int, stdin.readline().split())
    queue = deque()
    arr = list(map(int, stdin.readline().split()))
    for j in range(N):
        queue.append([arr[j], j])
    result = []
    while queue:
        if max(queue)[0] == queue[0][0]:
            result.append(queue.popleft())
        else:
            queue.append(queue.popleft())
    for i in range(N):
        if result[i][1] == M:
            print(i + 1)
            break