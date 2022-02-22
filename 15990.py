results = [[0, 0, 0] for _ in range(100001)]
results[1][0], results[1][1], results[1][2] = 1, 0, 0
results[2][0], results[2][1], results[2][2] = 0, 1, 0
results[3][0], results[3][1], results[3][2] = 1, 1, 1
for j in range(4, 100001):
    results[j][0] = (results[j - 1][1] + results[j - 1][2]) % 1000000009
    results[j][1] = (results[j - 2][0] + results[j - 2][2]) % 1000000009
    results[j][2] = (results[j - 3][0] + results[j - 3][1]) % 1000000009

T = int(input())
for i in range(T):
    num = int(input())
    result = (results[num][0] + results[num][1] + results[num][2]) % 1000000009
    print(result)
