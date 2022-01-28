N = int(input())
VPS = []
for i in range(N):
    VPS_input = input()
    for j in range(len(VPS_input)):
        if VPS_input[j] == '(':
            VPS.append('(')
        elif VPS_input[j] == ')':
            VPS.append(')')
    #print(VPS)
    a = 0
    while True:
        for i in range(len(VPS) - 1):
            if VPS[i] == '(' and VPS[i + 1] == ')':
                VPS.pop(i + 1)
                VPS.pop(i)
                break
            if i + 1 == len(VPS) - 1:
                a = 1
                break
        if a == 1:
            print('NO')
            break
        if len(VPS) == 0:
            print('YES')
            break
        elif len(VPS) == 1:
            print('NO')
            break
    VPS = []