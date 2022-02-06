from sys import stdin
input = stdin.readline
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().rstrip())))

result = []
def quad(x, y, N):
    mid = N // 2
    color = arr[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if arr[i][j] != color:
                result.append('(')
                quad(x, y, mid)
                quad(x, y + mid, mid)
                quad(x + mid, y, mid)
                quad(x + mid, y + mid, mid)
                result.append(')')
                return
    result.append(str(color))
    return

quad(0, 0, N)
print(''.join(result))