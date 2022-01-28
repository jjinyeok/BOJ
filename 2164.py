from collections import deque

N = int(input())
arr = deque(list(range(1, N + 1)))

while True:
    if len(arr) == 1:
        print(arr[0])
        break
    arr.popleft()
    arr.append(arr.popleft())
