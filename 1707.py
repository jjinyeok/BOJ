import sys
from collections import deque

# input
k = int(sys.stdin.readline())
for _ in range(k):
    answer = True
    v, e = map(int, sys.stdin.readline().split())
    graph = {i: [] for i in range(1, v + 1)}
    visited = [-1 for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    print(graph)

# 
for i in range(1, v + 1):
    

# output
    if answer:
        print('YES')
    else:
        print('NO')
