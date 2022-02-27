from sys import stdin
input = stdin.readline

UPPER = ord('A') #65
LOWER = ord('a') #97
NUMBER = ord('0') #48
SPACE = ord(' ') #32
count = 0
while count < 100:
    S = input().rstrip('\n')
    if S == '':
        break
    upper = 0
    lower = 0
    number = 0
    space = 0
    for i in S:
        alphabet = ord(i)
        if alphabet == 32:
            space += 1
        elif alphabet >= 97:
            lower += 1
        elif alphabet >= 65:
            upper += 1
        elif alphabet >= 48:
            number += 1
    print(str(lower) + ' ' + str(upper) + ' ' + str(number) + ' ' + str(space))
    count += 1
