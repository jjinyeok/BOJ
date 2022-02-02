from sys import stdin
import sys

arr = []
N = int(stdin.readline())
for i in range(N):
    arr.append(list(map(int, stdin.readline().split())))
result = []

for i in range(N):
    rank = 1
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    result.append(rank)

print(' '.join(map(str, result)))