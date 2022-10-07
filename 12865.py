import sys

n, k = map(int, sys.stdin.readline().split())
things = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    things.append([w, v])

knapsacks = [[[0, 0]] * (n + 1) for _ in range(k + 1)]
for i in range(1, k + 1):
    for j in range(1, n + 1):
        case_1 = knapsacks[i][j - 1]
        case_2 = [0, 0]
        if i - things[j - 1][0] >= 0 and knapsacks[i - things[j - 1][0]][j - 1][0] + things[j - 1][0] <= i:
            case_2 = [knapsacks[i - things[j - 1][0]][j - 1][0] + things[j - 1][0], knapsacks[i - things[j - 1][0]][j - 1][1] + things[j - 1][1]]
        if case_1[1] <= case_2[1]:
            knapsacks[i][j] = case_2
        else:
            knapsacks[i][j] = case_1

print(knapsacks[k][n][1])
