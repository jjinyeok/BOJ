from sys import stdin
input = stdin.readline
S = list(input().rstrip())
alphabets = [0] * 26
for alphabet in S:
    alphabets[ord(alphabet) - ord('a')] += 1
for alphabet in alphabets:
    print(alphabet, end=' ')
