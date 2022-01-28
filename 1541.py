values = input().split('-')
result_list = []
for value in values:
    if value.find('+') >= 0:
        element = map(int, value.split('+'))
        value = sum(element)
    else:
        value = int(value)
    result_list.append(value)

result = result_list[0] * 2
for result_element in result_list:
    result -= result_element
print(result)