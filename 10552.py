import sys

# input
n, m, p = map(int, sys.stdin.readline().split())
channels = [0 for _ in range(m + 1)]
for _ in range(n):
    pos, neg = map(int, sys.stdin.readline().split())
    if channels[neg] == 0:
        channels[neg] = pos

# make answer
answer = 0
while True:
    if channels[p] == 0:
        break
    elif channels[p] == -1:
        answer = -1
        break
    else:
        temp = channels[p] * 1
        channels[p] = -1
        p = temp
        answer += 1

# output
print(answer)
