from sys import stdin
input = stdin.readline

left_stack = list(input().rstrip())
right_stack = []

N = int(input())
for i in range(N):
    instructor = input().rstrip().split()
    if instructor[0] == 'L':
        if len(left_stack) > 0:
            right_stack.append(left_stack.pop())
    elif instructor[0] == 'D':
        if len(right_stack) > 0:
            left_stack.append(right_stack.pop())
    elif instructor[0] == 'B':
        if len(left_stack) > 0:
            left_stack.pop()
    elif instructor[0] == 'P':
        left_stack.append(instructor[1])

right_stack = list(reversed(right_stack))
print(''.join(left_stack + right_stack))
