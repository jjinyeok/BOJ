from sys import stdin
from collections import deque
input = stdin.readline
dic = {}
N = int(input())
arr = list(map(int, input().split()))
for number in arr:
    if number in dic:
        dic[number] += 1
    else:
        dic[number] = 1

queue = deque()
for i in range(N):
    queue.append([arr[i], dic[arr[i]], i])

stack = []
result = []
while queue:
    now = queue.popleft()
    if len(stack) == 0:
        stack.append(now)
        continue
    while stack:
        if stack[len(stack) - 1][1] < now[1]:
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

result.sort(key=lambda x: x[2])
for i in range(N):
    print(result[i][0], end=' ')
