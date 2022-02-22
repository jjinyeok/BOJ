from sys import stdin
input = stdin.readline
INF = 987654321

N = int(input())
cards = list(map(int, input().split()))
results = [INF] * N

for i in range(N):
    for j in range(i):
        if results[i] > cards[j] + results[i - j - 1]:
            results[i] = cards[j] + results[i - j - 1]
    if results[i] > cards[i]:
        results[i] = cards[i]

print(results[N - 1])
