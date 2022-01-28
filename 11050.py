N, K = map(int, input().split())
result = 1

if K == 0:
    result = 1
else:
    for i in range(K):
        result *= (N - i)
    for i in range(K):
        result /= (K - i)

print(int(result))