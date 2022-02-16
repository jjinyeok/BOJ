from sys import stdin
from itertools import combinations
input = stdin.readline

N, M = map(int, input().split())
lists = list(combinations(range(1, N + 1), M))
for list in lists:
    print(' '.join(map(str, list)))
