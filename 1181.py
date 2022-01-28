N = int(input())
arr = []
for i in range(N):
    arr.append(input())

len_arr = []
for i in range(N):
    len_arr.append(len(arr[i]))

result = []
result_col = []
for i in range(max(len_arr)):
    for j in range(N):
        if len(arr[j]) == i + 1:
            result_col.append(arr[j])
            result_col.sort()
    result.append(result_col)
    result_col = []

last_print = ''
for i in range(max(len_arr)):
    for j in range(len(result[i])):
        if last_print != result[i][j]:
            print(result[i][j])
            last_print = result[i][j]