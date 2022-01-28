import sys
N = int(sys.stdin.readline())
xys = []
for i in range(N):
    xy = list(map(int, sys.stdin.readline().split()))
    xys.append(xy)
xys.sort()
for i in range(N):
    print(xys[i][0], xys[i][1])