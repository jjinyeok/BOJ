a, b = map(int, input().split())
a_list = list(map(int, input().split()))

#print(a, b)
#print(a_list)
result = 0

for i in range(len(a_list)):
    for j in range(i + 1, len(a_list)):
        for k in range(j + 1, len(a_list)):
            if b - result > b - (a_list[i] + a_list[j] + a_list[k]) and b >= a_list[i] + a_list[j] + a_list[k]:
                result = a_list[i] + a_list[j] + a_list[k]

print(result)