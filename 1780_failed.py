from sys import stdin
from collections import deque
import heapq

n = int(stdin.readline())
answers = [0, 0, 0] # -1, 0, 1
papers = []
for _ in range(n):
    papers.append(list(map(int, stdin.readline().split())))

def same_check(start_xy, end_xy):
    start_x, start_y = start_xy
    end_x, end_y = end_xy
    value = papers[start_x][start_y]
    check = True
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if papers[i][j] != value:
                check = False
                break
    if check:
        answers[value + 1] += 1
    return check

n //= 3
q = []
heapq.heappush(q, [(0, 0), (0 + n - 1, 0 + n - 1), n])
heapq.heappush(q, [(0, n), (0 + n - 1, n + n - 1), n])
heapq.heappush(q, [(0, n * 2), (0 + n - 1, n * 2+ n - 1), n])
heapq.heappush(q, [(n, 0), (n + n - 1, 0 + n - 1), n])
heapq.heappush(q, [(n, n), (n + n - 1, n + n - 1), n])
heapq.heappush(q, [(n, n * 2), (n + n - 1, n * 2 + n - 1), n])
heapq.heappush(q, [(n * 2, 0), (n * 2 + n - 1, 0 + n - 1), n])
heapq.heappush(q, [(n * 2, n), (n * 2 + n - 1, n + n - 1), n])
heapq.heappush(q, [(n * 2, n * 2), (n * 2 + n - 1, n * 2+ n - 1), n])
while q:
    start_xy, end_xy, tmp = heapq.heappop(q)
    if same_check(start_xy, end_xy) == False:
        start_x, start_y = start_xy
        n = tmp * 1 // 3
        if n > 0:
            heapq.heappush(q, [(start_x + 0, start_y + 0), (start_x + 0 + n - 1, start_y + 0 + n - 1), n])
            heapq.heappush(q, [(start_x + 0, start_y + n), (start_x + 0 + n - 1, start_y + n + n - 1), n])
            heapq.heappush(q, [(start_x + 0, start_y + n * 2), (start_x + 0 + n - 1, start_y + n * 2+ n - 1), n])
            heapq.heappush(q, [(start_x + n, start_y + 0), (start_x + n + n - 1, start_y + 0 + n - 1), n])
            heapq.heappush(q, [(start_x + n, start_y + n), (start_x + n + n - 1, start_y + n + n - 1), n])
            heapq.heappush(q, [(start_x + n, start_y + n * 2), (start_x + n + n - 1, start_y + n * 2 + n - 1), n])
            heapq.heappush(q, [(start_x + n * 2, start_y + 0), (start_x + n * 2 + n - 1, start_y + 0 + n - 1), n])
            heapq.heappush(q, [(start_x + n * 2, start_y + n), (start_x + n * 2 + n - 1, start_y + n + n - 1), n])
            heapq.heappush(q, [(start_x + n * 2, start_y + n * 2), (start_x + n * 2 + n - 1, start_y + n * 2+ n - 1), n])

print('\n'.join(map(str, answers)))
