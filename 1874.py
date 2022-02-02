from sys import stdin
from collections import deque
N = int(stdin.readline())
result = []
stack = deque()
if_no = False
count = 0

for i in range(N):
    num = int(stdin.readline())
    while count < num:
        stack.append(count + 1)
        count += 1
        result.append('+')
    if stack[len(stack) - 1] == num:
        stack.pop()
        result.append('-')
    else:
        if_no = True

if if_no:
    print('NO')
else:
    print('\n'.join(result))