import sys

answer = [0, 0, 0]

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def check(x, y, n):
    global answer_minus_1, answer_0, answer_1
    temp = [0, 0, 0]
    for i in range(x, x + n):
        for j in range(y, y + n):
            temp[paper[i][j] + 1] += 1
    if temp[0] == n ** 2:
        answer[0] += 1
        return
    elif temp[1] == n ** 2:
        answer[1] += 1
        return
    elif temp[2] == n ** 2:
        answer[2] += 1
        return
    else:
        check(x, y, n // 3)
        check(x + n // 3, y, n // 3)
        check(x + (n // 3) * 2, y, n // 3)
        check(x, y + n // 3, n // 3)
        check(x + n // 3, y + n // 3, n // 3)
        check(x + (n // 3) * 2, y + n // 3, n // 3)
        check(x, y + (n // 3) * 2, n // 3)
        check(x + n // 3, y + (n // 3) * 2, n // 3)
        check(x + (n // 3) * 2, y + (n // 3) * 2, n // 3)

check(0, 0, n)
print('\n'.join(map(str, answer)))
