while True:
    array = list(map(int, input().split()))
    if array[0]==0 & array[1] == 0 & array[2] == 0:
        break
    arrayMax = max(array)
    if arrayMax ** 2 * 2 == array[0] ** 2 + array[1] ** 2 + array[2] ** 2:
        print('right')
    else:
        print('wrong')