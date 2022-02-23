from math import sqrt

i = 1
INF = 987654321
results = [INF] * 100001
while True:
    if i ** 2 > 100000:
        break
    results[i ** 2] = 1
    i += 1

for i in range(1, 100001):
    if results[i] == 1:
        checked = i
        continue
    else:
        for j in range(1, int(sqrt(checked)) + 1):
            if results[i] > results[j ** 2] + results[i - j ** 2]:
                results[i] = results[j ** 2] + results[i - j ** 2]

N = int(input())
print(results[N])
