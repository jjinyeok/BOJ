import sys
sys.setrecursionlimit(10 ** 5)

def dfs(i):
    global answers
    visited[i] = True
    cycle.append(i)
    next = preferences[i]
    if visited[next]:
        if next in cycle:
            answers += cycle[cycle.index(next) :]
        return
    else:
        dfs(next)

# input
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    preferences = [0]
    preferences += list(map(int, sys.stdin.readline().split()))
    visited = [False] * (n + 1)
    answers = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)
        
    print(n - len(answers))
