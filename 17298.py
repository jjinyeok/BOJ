from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
A = deque()
for i in range(N):
    A.append([arr[i], i])

stack = []
result = []
while A:
    now = A.popleft()
    if len(stack) == 0:
        stack.append(now)
        continue
    while stack:
        if stack[len(stack) - 1][0] < now[0]:
            element = stack.pop()
            element[0] = now[0]
            result.append(element)
        else:
            stack.append(now)
            break
    if len(stack) == 0:
        stack.append(now)
        continue

for element in stack:
    element[0] = -1
    result.append(element)

result.sort(key=lambda x: x[1])
for element in result:
    print(element[0], end=' ')
