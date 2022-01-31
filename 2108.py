from sys import stdin

N = int(stdin.readline())

arr = []
dic = dict()
for i in range(N):
    number = int(stdin.readline())
    arr.append(number)
    if number in dic:
        dic[number] += 1
    else:
        dic[number] = 1

arr.sort()
print(round(sum(arr) / N))
print(arr[N // 2])
dic_list = []
for x, y in dic.items():
    dic_list.append([y, x])
dic_list.sort(key=lambda x: (-x[0], x[1]))
if len(arr) == 1:
    print(dic_list[0][1])
else:
    if dic_list[0][0] != dic_list[1][0]:
        print(dic_list[0][1])
    else:
        print(dic_list[1][1])
print(max(arr) - min(arr))