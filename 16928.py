from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
snake_ladders = {}
for _ in range(n + m):
    now, target = map(int, stdin.readline().split())
    snake_ladders[now] = target

dices = [1, 2, 3, 4, 5, 6]
graph = [987654321 for _ in range(101)]
q = deque()
graph[1] = 0
q.append(1)
while q:
    now = q.popleft()
    for dice in dices:
        if now + dice <= 100:
            if now + dice in snake_ladders:
                if graph[now] + 1 < graph[snake_ladders[now + dice]]:
                    graph[snake_ladders[now + dice]] = graph[now] + 1
                    q.append(snake_ladders[now + dice])
            else:
                if graph[now] + 1 < graph[now + dice]:
                    graph[now + dice] = graph[now] + 1
                    q.append(now + dice)

print(graph[100])
