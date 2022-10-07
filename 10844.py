import sys
from copy import deepcopy

answers = [0 for _ in range(101)]
nows = {i: 1 for i in range(10)}
nows[0] = 0
for i in range(1, 101):
    answers[i] = sum(nows.values()) % 1000000000
    futures = {i: 0 for i in range(10)}
    for key, value in nows.items():
        if key - 1 in futures:
            futures[key - 1] += value
        if key + 1 in futures:
            futures[key + 1] += value
    nows = deepcopy(futures)

n = int(sys.stdin.readline())
print(answers[n])
