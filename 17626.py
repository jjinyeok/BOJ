from sys import stdin

answer = [0 for _ in range(50001)]
check_points = []
for i in range(1, 50001):
    if i ** (0.5) == int(i ** (0.5)):
        answer[i] = 1
        check_points.append(i)
    else:
        tmp = 987654321
        for check_point in check_points:
            if answer[check_point] + answer[i - check_point] < tmp:
                tmp = answer[check_point] + answer[i - check_point]
        answer[i] = tmp

n = int(stdin.readline())
print(answer[n])
