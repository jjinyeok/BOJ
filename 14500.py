import sys

r, c = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

def x_4_1(x, y):
    return graph[x][y] + graph[x][y + 1] + graph[x][y + 2] + graph[x][y + 3]

def x_3_2(x, y):
    cases = []
    cases.append(graph[x][y] + graph[x][y + 1] + graph[x][y + 2] + graph[x + 1][y + 2])
    cases.append(graph[x + 1][y] + graph[x + 1][y + 1] + graph[x + 1][y + 2] + graph[x][y + 2])
    cases.append(graph[x][y] + graph[x + 1][y] + graph[x][y + 1] + graph[x][y + 2])
    cases.append(graph[x][y] + graph[x + 1][y] + graph[x + 1][y + 1] + graph[x + 1][y + 2])
    cases.append(graph[x + 1][y] + graph[x + 1][y + 1] + graph[x][y + 1] + graph[x][y + 2])
    cases.append(graph[x][y] + graph[x][y + 1] + graph[x + 1][y + 1] + graph[x + 1][y + 2])
    cases.append(graph[x + 1][y] + graph[x + 1][y + 1] + graph[x + 1][y + 2] + graph[x][y + 1])
    cases.append(graph[x][y] + graph[x][y + 1] + graph[x][y + 2] + graph[x + 1][y + 1])
    return max(cases)

def x_2_2(x, y):
    return graph[x][y] + graph[x][y + 1] + graph[x + 1][y] + graph[x + 1][y + 1]

def x_2_3(x, y):
    cases = []
    cases.append(graph[x + 1][y] + graph[x][y + 1] + graph[x + 1][y + 1] + graph[x + 2][y + 1])
    cases.append(graph[x][y] + graph[x + 1][y] + graph[x + 2][y] + graph[x + 1][y + 1])
    cases.append(graph[x][y] + graph[x + 1][y] + graph[x + 1][y + 1] + graph[x + 2][y + 1])
    cases.append(graph[x][y + 1] + graph[x + 1][y + 1] + graph[x + 1][y] + graph[x + 2][y])
    cases.append(graph[x][y] + graph[x][y + 1] + graph[x + 1][y] + graph[x + 2][y])
    cases.append(graph[x][y] + graph[x][y + 1] + graph[x + 1][y + 1] + graph[x + 2][y + 1])
    cases.append(graph[x][y] + graph[x + 1][y] + graph[x + 2][y] + graph[x + 2][y + 1])
    cases.append(graph[x][y + 1] + graph[x + 1][y + 1] + graph[x + 2][y + 1] + graph[x + 2][y])
    return max(cases)

def x_1_4(x, y):
    return graph[x][y] + graph[x + 1][y] + graph[x + 2][y] + graph[x + 3][y]

answer = 0
for i in range(r):
    for j in range(c):
        if j + 3 <= c - 1:
            temp = x_4_1(i, j)
            if answer < temp:
                answer = temp
        if j + 2 <= c - 1 and i + 1 <= r - 1:
            temp = x_3_2(i, j)
            if answer < temp:
                answer = temp
        if j + 1 <= c - 1 and i + 1 <= r - 1:
            temp = x_2_2(i, j)
            if answer < temp:
                answer = temp
        if j + 1 <= c - 1 and i + 2 <= r - 1:
            temp = x_2_3(i, j)
            if answer < temp:
                answer = temp
        if i + 3 <= r - 1:
            temp = x_1_4(i, j)
            if answer < temp:
                answer = temp

print(answer)
