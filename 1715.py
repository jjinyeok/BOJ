import sys
import heapq

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    heapq.heappush(q, int(sys.stdin.readline()))

answer = 0
while True:
    if len(q) == 1:
        break
    num_1 = heapq.heappop(q)
    num_2 = heapq.heappop(q)
    answer += (num_1 + num_2)
    heapq.heappush(q, num_1 + num_2)

print(answer)
