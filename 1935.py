from sys import stdin
from collections import deque
N = int(stdin.readline())
M = list(stdin.readline().strip())
arr = []
for i in range(N):
    arr.append(int(stdin.readline()))

stack = deque()
for word in M:
    if word == '+':
        stack.append(stack.pop() + stack.pop())
    elif word == '-':
        #A-B
        tmp1 = stack.pop() #B
        tmp2 = stack.pop() #A
        stack.append(tmp2 - tmp1)
    elif word == '*':
        stack.append(stack.pop() * stack.pop())
    elif word == '/':
        #A/B
        tmp1 = stack.pop() #B
        tmp2 = stack.pop() #A
        stack.append(tmp2 / tmp1)
    else:
        stack.append(arr[ord(word) - ord('A')])

print('{:.2f}'.format(stack.pop()))