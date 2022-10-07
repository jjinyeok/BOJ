import sys

# input
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    preferences = [0]
    preferences += list(map(int, sys.stdin.readline().split()))

# 하나씩 확인하기
# 1. visited == False 경우
# 2. cycle 만들어질 때까지 돌리기
# 3. cycle이 만들어지면 (본인이 아니어도 됨) 사이클 안에 있는 node들은 visited = True
    for i in range(1, n + 1):
        if preferences[i] == -1 or preferences[i] == 0:
            pass
        else:
            flow = [i]
            while True:
                now = flow[-1]
                next = preferences[now]
                if preferences[next] == 0 or preferences[next] == -1:
                    for node in flow:
                        preferences[node] = -1
                    break
                elif preferences[now] in flow:
                    for j in range(len(flow)):
                        if preferences[now] == flow[j]:
                            cycle_index = j
                            break
                    for node in flow[cycle_index:]:
                        preferences[node] = 0
                    for node in flow[:cycle_index]:
                        preferences[node] = -1
                    break
                next = preferences[now]
                flow.append(next)

    answer = 0
    for preference in preferences:
        if preference == -1:
            answer += 1
    print(answer)
