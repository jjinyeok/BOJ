N = int(input())
tiling = [0] * 1001
tiling[1] = 1
tiling[2] = 3
for i in range(3, N + 1):
    tiling[i] = (tiling[i - 1] + tiling[i - 2] * 2) % 10007
print(tiling[N])
