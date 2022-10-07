import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    existed = [False] * k
    q_large, q_small = [], []
    
    for i in range(k):
        command, num = sys.stdin.readline().split()
        num = int(num)
        if command == 'I':
            heapq.heappush(q_large, (num * -1, i))
            heapq.heappush(q_small, (num, i))
            existed[i] = True

        elif command == 'D' and num == -1:
            while q_small:
                num, idx = heapq.heappop(q_small)
                if existed[idx] == True:
                    existed[idx] = False
                    break
        
        elif command == 'D' and num == 1:
            while q_large:
                num, idx = heapq.heappop(q_large)
                if existed[idx] == True:
                    existed[idx] = False
                    break

    large_answer, small_answer = -1, 1

    while q_large:
        num, idx = heapq.heappop(q_large)
        if existed[idx] == True:
            large_answer = num * -1
            break

    while q_small:
        num, idx = heapq.heappop(q_small)
        if existed[idx] == True:
            small_answer = num
            break
    
    if large_answer < small_answer:
        print('EMPTY')
    else:
        print(large_answer, small_answer)