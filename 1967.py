import sys
from collections import deque

# tree input
n = int(sys.stdin.readline())
tree = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    tree[parent].append([child, weight])

# based root, find children's scores
answer = 0
for parent, children in tree.items():
    q = deque([[parent, 0, -1]])
    results = {}
    while q:
        node, score, direction = q.popleft()
        # case1 : not leaf node
        if tree[node] != []:
            for child in tree[node]:
                if node == parent:
                    q.append([child[0], score + child[1], child[0]])
                else:
                    q.append([child[0], score + child[1], direction])
        # case2 : leaf node
        else:
            if direction in results:
                results[direction].append(score)
            else:
                results[direction] = [score]
    # calculate max score
    max_values = []
    for key, values in results.items():
        if key != -1:
            max_values.append(max(values))
    max_values.sort(reverse=True)
    if len(max_values) == 1:
        if max_values[0] > answer:
            answer = max_values[0]
    if len(max_values) > 1:
        if max_values[0] + max_values[1] > answer:
            answer = max_values[0] + max_values[1]

# output
print(answer)
