import sys

n, k = map(int, sys.stdin.readline().split())
counts = [-1 for _ in range(n + 1)]
coins = []
for _ in range(n):
    coin = int(sys.stdin.readline())
    counts[coin] = 1
    coins.append(coin)

for i in range(1, n + 1):
    pass