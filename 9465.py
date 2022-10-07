import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    stickers = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    answers = [[0, 0] for _ in range(n)]
    answers[0][0], answers[0][1] = stickers[0][0], stickers[1][0]
    if n >= 2:
        answers[1][0], answers[1][1] = stickers[1][0] + stickers[0][1], stickers[1][1] + stickers[0][0]
    if n >= 3:
        for i in range(2, n):
            answers[i][0] = max(answers[i - 1][1] + stickers[0][i], max(answers[i - 2]) + stickers[0][i])
            answers[i][1] = max(answers[i - 1][0] + stickers[1][i], max(answers[i - 2]) + stickers[1][i])
    print(max(answers[n - 1]))
