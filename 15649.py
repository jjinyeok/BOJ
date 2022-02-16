from sys import stdin
from itertools import permutations
input = stdin.readline

N, M = map(int, input().split())
lists = list(permutations(range(1, N + 1), M))
for list in lists:
    print(' '.join(map(str, list)))
