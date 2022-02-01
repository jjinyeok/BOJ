from sys import stdin

while True:
    sentence = list(stdin.readline().rstrip('\n'))
    if sentence[0] == "." and len(sentence) == 1:
        break
    stack = []
    for i in range(len(sentence)):
        if sentence[i] == '(':
            stack.append('(')
        if sentence[i] == '[':
            stack.append('[')
        if sentence[i] == ')':
            if stack and stack.pop() == '(':
                pass
            else:
                print('no')
                break
        if sentence[i] == ']':
            if stack and stack.pop() == '[':
                pass
            else:
                print('no')
                break
        if len(stack) == 0 and i == len(sentence) - 1:
            print('yes')
        if len(stack) != 0 and i == len(sentence) - 1:
            print('no')