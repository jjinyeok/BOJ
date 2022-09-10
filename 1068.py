import sys
from collections import deque
n = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))
remove_node = int(sys.stdin.readline())

node_dic = {i: [] for i in range(n)}
for i in range(n):
    if nodes[i] != -1:
        node_dic[nodes[i]].append(i)

q = deque([remove_node])
while q:
    parent = q.popleft()
    for child in node_dic[parent]:
        q.append(child)
    node_dic[parent] = [-1]

answer = 0
for key, value in node_dic.items():
    if remove_node in value:
        value.remove(remove_node)
    if value == []:
        answer += 1
print(answer)
