from sys import stdin

N = int(stdin.readline())
xys = []

for i in range(N):
    xy = list(map(int, stdin.readline().split()))
    xys.append(xy)

xys.sort(key=lambda x : (x[1], x[0]))

for i in range(N):
    print(str(xys[i][0]) + ' ' + str(xys[i][1]))