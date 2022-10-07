import sys

scores = [1 for _ in range(1000001)]
for i in range(2, 1000001):
    scores[i] = (scores[i - 1] + scores[i - 2]) % 15746

n = int(sys.stdin.readline())
print(scores[n])
