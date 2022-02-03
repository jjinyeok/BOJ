from sys import stdin
K, N = map(int, stdin.readline().split())
lans = [int(stdin.readline()) for _ in range(K)]

start = 1
end = max(lans)
while start <= end:
    mid = (start + end) // 2
    lines = 0
    for lan in lans:
        lines += lan // mid
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)