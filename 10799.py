from sys import stdin
input = stdin.readline

brackets = list(input().rstrip())
stack = []
result = 0
for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append('(')
    else:
        if brackets[i - 1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)
