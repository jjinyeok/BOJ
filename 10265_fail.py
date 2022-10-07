import sys
from collections import deque

# input
n, k = map(int, sys.stdin.readline().split())
visited = [True] + [False] * n
graph = {i: [] for i in range(1, n + 1)}
preferences = list(map(int, sys.stdin.readline().split()))
for i in range(1, n + 1):
    if i != preferences[i - 1]:
        graph[i].append(preferences[i - 1])
        graph[preferences[i - 1]].append(i)

# make counts
counts = []
for i in range(1, n + 1):
    if visited[i] == False:
        q = deque([i])
        count = 0
        while q:
            now = q.popleft()
            visited[now] = True
            count += 1
            for next in graph[now]:
                if visited[next] == False:
                    q.append(next)
                    visited[next] = True
        counts.append(count)
len_counts = len(counts)
print(counts)
# knapsack
knapsacks = [[0] * (len_counts + 1) for _ in range(k + 1)]
for i in range(1, k + 1):
    for j in range(1, len_counts + 1):
        case1 = knapsacks[i][j - 1]
        case2 = 0
        if counts[j - 1] + knapsacks[i][j - 1] <= k:
            case2 = counts[j - 1] + knapsacks[i][j - 1]
        knapsacks[i][j] = max(case1, case2)
print(knapsacks[k][len_counts])
