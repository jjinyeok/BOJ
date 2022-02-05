from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
pwbook = dict()
for i in range(N):
    address, password = input().rstrip().split()
    pwbook[address] = password

for i in range(M):
    find_address = input().rstrip()
    print(pwbook[find_address])