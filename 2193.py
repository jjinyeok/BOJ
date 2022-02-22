N = int(input())

results = [0] * (N + 1)
why_not = [0] * (N + 1)

for i in range(1, N + 1):
    results[i] = 2 ** (i - 1)
    why_not[i] = results[i - 1]
    for j in range(i):
        why_not[i] += why_not[j]
    results[i] -= why_not[i]

print(results[N])
