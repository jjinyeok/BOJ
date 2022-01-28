N, M = map(int, input().split())

a = min(N, M)
while True:
    if max(N, M) % a == 0 and min(N, M) % a == 0:
        print(a)
        break
    a -= 1

a = max(N, M)
while True:
    if a % max(N, M) == 0 and a % min(N, M) == 0:
        print(a)
        break
    a += 1