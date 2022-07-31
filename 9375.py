from re import L
from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    wear_dic = {}
    for _ in range(n):
        wear, kind = stdin.readline().split()
        if kind in wear_dic:
            wear_dic[kind] += 1
        else:
            wear_dic[kind] = 1
    answer = 1
    for k, v in wear_dic.items():
        answer *= (v + 1)
    print(answer - 1)
