from sys import stdin
input = stdin.readline
result = []

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

def cut(x, y, N):
    color = arr[x][y]
    for i in range(x, N + x):
        for j in range(y, N + y):
            if color != arr[i][j]:
                cut(x, y, N // 2)
                cut(x + N // 2, y, N // 2)
                cut(x, y + N // 2, N // 2)
                cut(x + N // 2, y + N // 2, N // 2)
                return
    if color == 1:
        result.append(1)
    elif color == 0:
        result.append(0)
    return

cut(0, 0, N)
print(result.count(0))
print(result.count(1))