import sys
from collections import deque

# input
n = int(sys.stdin.readline())
populations = list(map(int, sys.stdin.readline().split()))
connections = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    connections[a].append(b)
    connections[b].append(a)

# make tree
tree = {i: [] for i in range(1, n + 1)}
visited = [False for _ in range(n + 1)]
layer = [0 for _ in range(n + 1)]
q = deque([1])
visited[1] = True
layer[1] = 1
layers = {1: [1]}
while q:
    now = q.popleft()
    for idx in connections[now]:
        if visited[idx] == False and idx != now:
            tree[now].append(idx)
            visited[idx] = True
            layer[idx] = layer[now] + 1
            if layer[idx] not in layers:
                layers[layer[idx]] = [idx]
            else:
                layers[layer[idx]].append(idx)
            q.append(idx)

# make answer dynamic programming
answers = [0 for _ in range(n + 1)]
max_layer = max(layer)
for idx in range(max_layer, 0, -1):
    for node in layers[idx]:
        # case1: leaf node
        if tree[node] == []:
            answers[node] = populations[node - 1]
        else:
            temp_answer_1 = 0
            for child in tree[node]:
                temp_answer_1 += answers[child]
            temp_answer_2 = populations[node - 1]
            for child in tree[node]:
                for child_child in tree[child]:
                    temp_answer_2 += answers[child_child]
            answers[node] = max(temp_answer_1, temp_answer_2)

# output
print(answers[1])
