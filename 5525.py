from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline().strip()

pn = 'I'
for _ in range(n):
    pn += 'OI'
len_pn = len(pn)

answer = 0
i = 0
while i < m - len(pn):
    check = True
    for j in range(len_pn):
        if s[j + i] != pn[j]:
            check = False
            break
    if check:
        answer += 1
        i += 2
    else:
        i += 1

print(answer)
