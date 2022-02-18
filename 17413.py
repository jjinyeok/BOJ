from sys import stdin
input = stdin.readline
S = list(reversed(list(input().rstrip())))
result = []
tmp_word = []

if S[len(S) - 1] == '<':
    tagOn = True
else:
    tagOn = False
while S:
    character = S.pop()
    if tagOn == True:
        result.append(character)
        if character == '>':
            tagOn = False
    elif tagOn == False:
        if character == ' ':
            while tmp_word:
                result.append(tmp_word.pop())
            result.append(character)
            continue
        elif character == '<':
            while tmp_word:
                result.append(tmp_word.pop())
            result.append(character)
            tagOn = True
            continue
        tmp_word.append(character)
if tmp_word != []:
    while tmp_word:
        result.append(tmp_word.pop())

print(''.join(result))
