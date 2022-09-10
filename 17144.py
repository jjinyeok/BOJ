from sys import stdin

r, c, t = map(int, stdin.readline().split())
graph = [] #[value, []]
air_cleaner = []
for i in range(r):
    values = list(map(int, stdin.readline().split()))
    tmp_list = []
    for value in values:
        tmp_list.append([value, []])
        if value == -1:
            air_cleaner.append(i)
    graph.append(tmp_list)

x = 0
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
while x != t:
    for i in range(r):
        for j in range(c):
            if graph[i][j][0] != -1:
                count = 0
                for k in range(4):
                    if i + dx[k] >= 0 and j + dy[k] >= 0 and i + dx[k] <= r - 1 and j + dy[k] <= c - 1 and graph[i + dx[k]][j + dy[k]][0] != -1:
                        count += 1
                        graph[i + dx[k]][j + dy[k]][1].append(graph[i][j][0] // 5)
                graph[i][j][1].append(graph[i][j][0] // 5 * count * (-1))

    for i in range(r):
        for j in range(c):
            graph[i][j][0] += sum(graph[i][j][1])
    
    for i in range(r):
        for j in range(c):
            graph[i][j][1] = []
    
    up_air_cleaner, down_air_cleaner = air_cleaner

    # green area -> o
    for i in range(up_air_cleaner - 1, -1, -1):
        graph[i + 1][0] = graph[i][0]
    # blue area
    graph[0][:c - 1] = graph[0][1:]
    # red area
    for i in range(1, up_air_cleaner + 1):
        graph[i - 1][c - 1] = graph[i][c - 1]
    # black area
    graph[up_air_cleaner][1:] = [[0, []]] + graph[up_air_cleaner][1:c-1]
    graph[up_air_cleaner][0] = [-1, []]

    # down
    # blue area
    for i in range(down_air_cleaner + 1, r):
        graph[i - 1][0] = graph[i][0]
    # red area
    graph[r - 1][:c-1] = graph[r-1][1:c]
    # black area
    for i in range(r - 2, down_air_cleaner - 1, -1):
        graph[i + 1][c - 1] = graph[i][c - 1]
    # green area
    graph[down_air_cleaner][1:] = [[0, []]] + graph[down_air_cleaner][1:c-1]
    graph[down_air_cleaner][0] = [-1, []]
    
    x += 1

answer = 0
for i in range(r):
    for j in range(c):
        answer += graph[i][j][0]

print(answer + 2)
