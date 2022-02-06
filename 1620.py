from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
num2name = dict()
name2num = dict()
for i in range(1, N + 1):
    name = input().rstrip()
    num2name[i] = name
    name2num[name] = i

for i in range(M):
    tmp = input().rstrip()
    if ord(tmp[0]) >= ord('0') and ord(tmp[0]) <= ord('9'):
        print(num2name[int(tmp)])
    else:
        print(name2num[tmp])
