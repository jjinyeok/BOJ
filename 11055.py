from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
results = [0] * (N)
results[0] = arr[0]
for i in range(1, len(arr)):
    results[i] = arr[i]
    sum = 0
    for j in range(i):
        if arr[i] > arr[j]:
            if sum < results[j]:
                sum = results[j]
    results[i] += sum

print(max(results))
