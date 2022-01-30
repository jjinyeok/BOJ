from sys import stdin

N = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
cardNumberDic = dict()
for card in cards:
    if card not in cardNumberDic:
        cardNumberDic[card] = 1
    else:
        cardNumberDic[card] += 1

M = int(stdin.readline())
finds = list(map(int, stdin.readline().split()))
arr = []
for find in finds:
    if find in cardNumberDic:
        arr.append(cardNumberDic[find])
    else:
        arr.append(0)

print(' '.join(map(str, arr)))