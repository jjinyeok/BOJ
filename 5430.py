from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())
for i in range(T):
    # input
    instructors = deque()
    tmp_instructors = input().rstrip()
    for tmp_instructor in tmp_instructors:
        instructors.append(tmp_instructor)
    N = int(input())
    arrs = deque()
    tmptmp_arrs = input().rstrip()
    if N == 1:
        arrs.append(tmptmp_arrs.lstrip('[').rstrip(']'))
    elif N >= 2:
        tmp_arrs = tmptmp_arrs.lstrip('[').rstrip(']').split(',')
        for tmp_arr in tmp_arrs:
            arrs.append(tmp_arr)
    # calculation
    r_count = 0
    error_count = 0
    while instructors:
        instructor = instructors.popleft()
        if instructor == 'R':
            r_count += 1
        elif instructor == 'D':
            if len(arrs) == 0:
                error_count = 1
                break
            else:
                if r_count % 2 == 0:
                    arrs.popleft()
                else:
                    arrs.pop()
    if error_count == 1:
        print('error')
    else:
        if r_count % 2 == 1:
            arrs.reverse()
        print('[' + ','.join(list(arrs)) + ']')
