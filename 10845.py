from collections import deque
import sys

N = int(sys.stdin.readline())
arr = deque()
for i in range(N):
    statement = sys.stdin.readline().split()
    if statement[0] == 'push':
        arr.append(int(statement[1]))
    elif statement[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif statement[0] == 'size':
        print(len(arr))
    elif statement[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif statement[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif statement[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr) - 1])