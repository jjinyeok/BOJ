import sys

N = int(sys.stdin.readline())
dic = [0] * 10001

for i in range(N):
    number = int(sys.stdin.readline())
    dic[number] += 1
    
for i in range(10001):
    for j in range(dic[i]):
        sys.stdout.write("%s\n" %i)
