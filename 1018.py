N, M = map(int, input().split())
result = 10000
chess_pan_1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

chess_pan_2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

arr = []
arr_col = []
for i in range(N):
    input_col = input()
    for j in range(len(input_col)):
        if input_col[j] == 'B':
            arr_col.append('B')
        elif input_col[j] == 'W':
            arr_col.append('W')
    arr.append(arr_col)
    arr_col = []

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        count_1 = 0
        count_2 = 0
        for a in range(8):
            for b in range(8):
                if chess_pan_1[a][b] != arr[a + i][b + j]:
                    count_1 += 1
                if chess_pan_2[a][b] != arr[a + i][b + j]:
                    count_2 += 1
        result = min(count_1, count_2, result)

print(result)