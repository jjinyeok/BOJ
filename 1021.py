from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
queue = deque()
for i in range(1, N + 1):
    queue.append(i)
nums = list(map(int, stdin.readline().split()))

result = 0
for num in nums:
    while True:
        if queue[0] == num:
            queue.popleft()
            break
        else:
            if queue.index(num) < len(queue) / 2:
                while queue[0] != num:
                    queue.append(queue.popleft())
                    result += 1
            else:
                while queue[0] != num:
                    queue.appendleft(queue.pop())
                    result += 1

print(result)