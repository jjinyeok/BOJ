from sys import stdin

N = int(stdin.readline())
count = 0
i = 0
result = 0
while count != N:
    i += 1
    if '666' in str(i):
        count += 1
        result = i

print(i)