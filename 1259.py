while True:
    element = input()
    if element == '0':
        break
    a = 1
    if len(element) % 2 == 0:
        for i in range(len(element)//2):
            if element[i] != element[len(element) - 1 - i]:
                a = 0
        if a == 1:
            print('yes')
        else:
            print('no')
    else:
        for i in range(len(element)//2 + 1):
            if element[i] != element[len(element) - 1 - i]:
                a = 0
        if a == 1:
            print('yes')
        else:
            print('no')