from sys import stdin
from collections import deque
input = stdin.readline

gears = []
for i in range(4):
    tmpgear = list(input().rstrip())
    queue = deque()
    for i in range(8):
        queue.append(tmpgear[i])
    gears.append(queue)

K = int(input())
for i in range(K):
    gear, direction = map(int, input().split())
    gear -= 1

    arr = []
    for i in range(3):
        if gears[i][2] != gears[i + 1][6]:
            arr.append(True)
        else:
            arr.append(False)

    left_gear = gear * 1
    left_direction = direction * 1
    while left_gear >= 1:
        if left_direction == -1:
            if arr[left_gear - 1] == True:
                gears[left_gear - 1].appendleft(gears[left_gear - 1].pop())
                left_gear -= 1
                left_direction *= (-1)
            else:
                break
        elif left_direction == 1:
            if arr[left_gear - 1] == True:
                gears[left_gear - 1].append(gears[left_gear - 1].popleft())
                left_gear -= 1
                left_direction *= (-1)
            else:
                break
    
    right_gear = gear * 1
    right_direction = direction * 1
    while right_gear <= 2:
        if right_direction == -1:
            if arr[right_gear] == True:
                gears[right_gear + 1].appendleft(gears[right_gear + 1].pop())
                right_gear += 1
                right_direction *= (-1)
            else:
                break
        elif right_direction == 1:
            if arr[right_gear] == True:
                gears[right_gear + 1].append(gears[right_gear + 1].popleft())
                right_gear += 1
                right_direction *= (-1)
            else:
                break
    
    if direction == 1:
        gears[gear].appendleft(gears[gear].pop())
    elif direction == -1:
        gears[gear].append(gears[gear].popleft())

result = 0
for i in range(4):
    if gears[i][0] == '1':
        result += 2 ** i
print(result)
