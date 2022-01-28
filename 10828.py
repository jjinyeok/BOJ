import sys
from collections import deque

N = int(input())
arr = deque()
for i in range(N):
    statement = sys.stdin.readline().split()
    if statement[0] == 'push':
        arr.append(statement[1])
    elif statement[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif statement[0] == 'size':
        print(len(arr))
    elif statement[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif statement[0] == 'top':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr) - 1])
    statement = []