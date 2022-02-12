from sys import stdin
from collections import deque
input = stdin.readline

A, B = map(int, input().split())
queue = deque()

result = -1
queue = deque()
queue.append([A, 0])
while queue:
    integer, count = queue.popleft()
    if integer * 10 + 1 == B:
        result = count + 2
        break
    if integer * 2 == B:
        result = count + 2
        break
    if integer * 10 + 1 < B:
        queue.append([integer * 10 + 1, count + 1])
    if integer * 2 < B:
        queue.append([integer * 2, count + 1])

print(result)
