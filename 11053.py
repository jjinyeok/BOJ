from sys import stdin
N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
result = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j] and result[i] < result[j] + 1:
                result[i] = result[j] + 1
print(max(result))