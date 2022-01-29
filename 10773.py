from sys import stdin
N = int(stdin.readline())

arr = []
for i in range(N):
    tmp = int(stdin.readline())
    if tmp == 0:
        arr.pop()
    else:
        arr.append(tmp)

print(sum(arr))