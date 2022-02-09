from sys import stdin
import heapq
input = stdin.readline

N = int(input())
q = []
for i in range(N):
    x = int(input())
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            output = heapq.heappop(q)
            print(output)
    else:
        heapq.heappush(q, x)
