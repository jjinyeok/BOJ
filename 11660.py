from sys import stdin
N, M = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
result = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        result[i + 1][j + 1] = result[i][j + 1] + result[i + 1][j] - result[i][j] + arr[i][j]
for i in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(result[x2][y2] - result[x1 - 1][y2] - result[x2][y1 - 1] + result[x1 - 1][y1 - 1])
