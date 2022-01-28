from collections import deque
import sys

arr = deque()
N = int(sys.stdin.readline())
for i in range(N):
    statement = sys.stdin.readline().split()
    if statement[0] == 'push_front':
        arr.appendleft(int(statement[1]))
    elif statement[0] == 'push_back':
        arr.append(int(statement[1]))
    elif statement[0] == 'pop_front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif statement[0] == 'pop_back':
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