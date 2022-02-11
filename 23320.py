from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
X, Y = map(int, input().split())

result1 = N * X // 100
result2 = 0
for i in range(N):
    if A[i] >= Y:
        result2 += 1

print(result1, result2)
