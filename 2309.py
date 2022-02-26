from itertools import combinations
from sys import stdin
input = stdin.readline
combs = list(combinations(range(9), 7))


dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

results = []
for comb in combs:
    sum = 0
    for height in comb:
        sum += dwarfs[height]
    if sum == 100:
        for i in comb:
            results.append(dwarfs[i])
        break

results.sort()
for i in range(7):
    print(results[i])
