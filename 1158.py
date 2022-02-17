from sys import stdin
from collections import deque
input = stdin.readline
N, K = map(int, input().split())
queue = deque()
for i in range(1, N + 1):
    queue.append(i)
result = []
while queue:
    for i in range(K - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print('<' + ', '.join(map(str, result)) + '>')
