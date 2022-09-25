# fail: 메모리 초과
# 굳이 Tree구조를 만들어서 DFS를 돌릴 필요가 없음
# 리스트 형태로도 가능함

import sys
sys.setrecursionlimit(150000)

# input
n, r, q = map(int, sys.stdin.readline().split())
connect = {}
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    if a in connect: connect[a].append(b)
    else: connect[a] = [b]
    if b in connect: connect[b].append(a)
    else: connect[b] = [a]

# make tree
tree = {}
def make_tree(current_node, parent_node):
    for node in connect[current_node]:
        if node != parent_node:
            if current_node not in tree:
                tree[current_node] = [node]
            else:
                tree[current_node].append(node)
            make_tree(node, current_node)
make_tree(r, -1)

# calculate count
answers = [0 for _ in range(n + 1)]
def dfs(node):
    answers[node] = 1
    if node not in tree:
        return 1
    else:
        for child in tree[node]:
            answers[node] += dfs(child)
        return answers[node]
dfs(r)

# output
for _ in range(q):
    root = int(sys.stdin.readline())
    print(answers[root])
 