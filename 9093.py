from sys import stdin
input = stdin.readline

T = int(input())
for i in range(T):
    sentence = list(input().rstrip().split())
    result = []
    for word in sentence:
        result.append(''.join(reversed(word)))
    print(' '.join(result))
