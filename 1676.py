N = int(input())
factorial = [1] * (N + 1)
for i in range(1, N + 1):
    factorial[i] = factorial[i - 1] * i
result = 0
while True:
    if factorial[N] % 10 != 0:
        break
    else:
        factorial[N] //= 10
        result += 1
print(result)
