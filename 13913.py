from sys import stdin
from collections import deque
input = stdin.readline

N, K = map(int, input().split())
distance = [-1] * 100001
before = [-1] * 100001

def bfs(start, end):
    queue = deque()
    queue.append(start)
    distance[start] = 0
    before[start] = 0
    while True:
        now = queue.popleft()
        if now - 1 >= 0:
            if distance[now - 1] == -1 and before[now - 1] == -1:
                distance[now - 1] = distance[now] + 1
                before[now - 1] = now
                queue.append(now - 1)
                if now - 1 == end:
                    return now - 1
        if now + 1 <= 100000:
            if distance[now + 1] == -1 and before[now + 1] == -1:
                distance[now + 1] = distance[now] + 1
                before[now + 1] = now
                queue.append(now + 1)
                if now + 1 == end:
                    return now + 1
        if now >= 1 and now <= 50000:
            if distance[now * 2] == -1 and before[now * 2] == -1:
                distance[now * 2] = distance[now] + 1
                before[now * 2] = now
                queue.append(now * 2)
                if now * 2 == end:
                    return now * 2

if N == K:
    print(0)
    print(K)
else:
    result = bfs(N, K)
    print(distance[result])
    results = []
    results.append(K)
    x = result
    for i in range(distance[result]):
        before[x]
        x = before[x]
        results.append(x)
    results = list(reversed(results))
    print(' '.join(map(str, results)))
