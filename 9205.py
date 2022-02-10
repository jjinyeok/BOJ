from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    start = list(map(int, input().split()))
    beer = []
    for i in range(N):
        beer.append(list(map(int, input().split())))
    end = list(map(int, input().split()))
    visited = [False] * N

    queue = deque()
    queue.append(start)
    happy = False
    while queue:
        x, y = queue.popleft()
        if abs(end[0] - x) + abs(end[1] - y) <= 1000:
            happy = True
            break
        for i in range(N):
            if abs(beer[i][0] - x) + abs(beer[i][1] - y) <= 1000:
                if visited[i] == False:
                    queue.append(beer[i])
                    visited[i] = True
    
    if happy == True:
        print('happy')
    else:
        print('sad')