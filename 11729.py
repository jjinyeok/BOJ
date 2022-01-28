def hanoi(number, _from, _via, _to):
    if number == 1:
        print(_from, _to)
    else:
        hanoi(number - 1, _from, _to, _via)
        print(_from, _to)
        hanoi(number - 1, _via, _from, _to)

n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 2, 3)