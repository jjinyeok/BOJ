import sys
from collections import deque

# input
n = int(sys.stdin.readline())
connections = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    connections[a].append(b)
    connections[b].append(a)

# make tree
tree = {i: [] for i in range(1, n + 1)}
visited = [False for _ in range(n + 1)]
visited[1] = True
layer = [0 for _ in range(n + 1)]
layer[1] = 1
layers = {1: [1]}
q = deque([1])
while q:
    node = q.popleft()
    for child in connections[node]:
        if visited[child] == False:
            tree[node].append(child)
            layer[child] = layer[node] + 1
            if layer[child] not in layers:
                layers[layer[child]] = [child]
            else:
                layers[layer[child]].append(child)
            visited[child] = True
            q.append(child)

# caculate early addapter by dynamic tree
answers_early_adapter = {i: 1 for i in range(1, n + 1)}
answers_not_early_adapter = {i: 0 for i in range(1, n + 1)}
for i in range(max(layer), 0, -1):
    for node in layers[i]:
        if tree[node] == []:
            answers_early_adapter[node] = 1
            answers_not_early_adapter[node] = 0
        for child in tree[node]:
            answers_early_adapter[node] += min(answers_early_adapter[child], answers_not_early_adapter[child])
            answers_not_early_adapter[node] += answers_early_adapter[child]

# output
print(min(answers_early_adapter[1], answers_not_early_adapter[1]))
