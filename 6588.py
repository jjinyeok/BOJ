from sys import stdin
from math import sqrt
input = stdin.readline

primeNumber = []
for i in range(3, 1000001):
    checked = 0
    for j in range(1, int(sqrt(i)) + 1):
        if i % j == 0 and j != 1:
            checked = 1
            break
    if checked == 0:
        primeNumber.append(i)

while True:
    N = int(input().strip())
    if N == 0:
        break
    else:
        for num1 in primeNumber:
            checked = 0
            for num2 in primeNumber:
                if num1 + num2 > N:
                    break
                if num1 + num2 == N:
                    checked = 1
                    break
            if checked == 1:
                print(str(N) + ' = ' + str(num1) + ' + ' + str(num2))
                break
        if num1 == primeNumber[len(primeNumber) - 1]:
            print("Goldbach's conjecture is wrong.")
            break
