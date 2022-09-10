from collections import deque
import sys

case_num = 1
while True:
    tree_count = 0
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break

    # Tree Input
    graph = {i : [] for i in range(1, n + 1)}
    visited = [False for _ in range(n)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b); graph[b].append(a)

    # Tree Verification
    for i in range(1, n + 1):
        duplication_check = False
        if visited[i - 1] == False:
            q = deque([[i, 0]]) # now, prev
            while q:
                now, prev = q.popleft()
                visited[now - 1] = True
                for next in graph[now]:
                    if next != prev:
                        q.append([next, now])
                        if visited[next - 1]:
                            duplication_check = True
                if duplication_check: break
            if not duplication_check: tree_count += 1
    
    # Ouptut
    if tree_count > 1:
        print(f'Case {case_num}: A forest of {tree_count} trees.')
    elif tree_count == 1:
        print(f'Case {case_num}: There is one tree.')
    else:
        print(f'Case {case_num}: No trees.')
    case_num += 1
