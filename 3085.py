from sys import stdin
input = stdin.readline

N = int(input())
candies = []
for i in range(N):
    candies.append(list(input().rstrip()))

def search(candies ,N):
    result = 0
    for i in range(N):
        tmp = 1
        for j in range(N - 1):
            if candies[i][j] == candies[i][j + 1]:
                tmp += 1
                result = max(result, tmp)
            else:
                tmp = 1
    for i in range(N):
        tmp = 1
        for j in range(N - 1):
            if candies[j][i] == candies[j + 1][i]:
                tmp += 1
                result = max(result, tmp)
            else:
                tmp = 1
    return result

result = 0
for i in range(N):
    for j in range(N):
        if j + 1 < N and candies[i][j] != candies[i][j + 1]:
            candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]
            if search(candies, N) > result:
                result = search(candies, N)
            candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]

for i in range(N):
    for j in range(N):
        if j + 1 < N and candies[j][i] != candies[j + 1][i]:
            candies[j][i], candies[j + 1][i] = candies[j + 1][i], candies[j][i]
            if search(candies, N) > result:
                result = search(candies, N)
            candies[j][i], candies[j + 1][i] = candies[j + 1][i], candies[j][i]

print(result)
