N = int(input())

for i in range(N + 1):
    result = i
    a = i
    while i >= 1:
        result += i % 10
        i //= 10
    if result == N:
        print(a)
        break
    if a == N:
        print(0)
        break