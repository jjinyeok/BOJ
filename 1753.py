from sys import stdin
import heapq
input = stdin.readline
INF = 987654321

V, E = map(int, input().split())
K = int(input())

visited = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    visited[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if visited[now] < dist:
            continue
        for i in graph[now]:
            if dist + i[1] < visited[i[0]]:
                visited[i[0]] = dist + i[1]
                heapq.heappush(q, [visited[i[0]], i[0]])

dijkstra(K)
for i in range(1, V + 1):
    if visited[i] == INF:
        print('INF')
    else:
        print(visited[i])
