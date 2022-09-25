import sys
sys.setrecursionlimit(10**5)

# input - make graph
n, r, q = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs - caculate count
answers = [0 for _ in range(n + 1)]
count = 1
def dfs(current_node, parent_node):
    count = 1
    for node in graph[current_node]:
        if node != parent_node:
            count += dfs(node, current_node)
            # dfs(node, current_node)
    answers[current_node] = count
    return count
dfs(r, -1)

# output
for _ in range(q):
    qurey = int(sys.stdin.readline())
    print(answers[qurey])
