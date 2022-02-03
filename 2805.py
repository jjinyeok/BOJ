from sys import stdin
N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

start = 1
end = max(trees)
while start <= end:
    mid = (start + end) // 2
    felling = 0
    for tree in trees:
        if tree > mid:
            felling += tree - mid

    if felling >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)