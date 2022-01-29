import sys
N, K = map(int, sys.stdin.readline().split())

arr = list(range(1, N + 1))
current = K - 1
result = []
result.append(arr.pop(current))
while len(arr) != 0:
    current = (current + K - 1) % len(arr)
    result.append(arr.pop(current))

print('<' + ', '.join(map(str, result)) + '>')