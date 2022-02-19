while True:
    try:
        N = int(input())
    except EOFError:
        break
    string = '1'
    while True:
        if int(string) % N == 0:
            print(len(string))
            break
        string += '1'
