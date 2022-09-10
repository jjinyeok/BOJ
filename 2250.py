import sys
from collections import deque

# input
n = int(sys.stdin.readline())
tree = {}
for _ in range(n):
    parent, left_child, right_child = map(int, sys.stdin.readline().split())
    tree[parent] = [left_child, right_child]

# find root
value_1 = [value[0] for value in tree.values()]
value_2 = [value[1] for value in tree.values()]
nodes = [key for key in tree.keys()]
for i in nodes:
    try: 
        list(set(value_1 + value_2)).index(i)
    except:
        root = i

# tree traversal
q = deque([root])
answers = [[1, 1] for _ in range(10001)]
answers[root] = [1, 1]
while q:
    node = q.popleft()
    left_child, right_child = tree[node]
    child_height = answers[node][0] + 1
    if left_child != -1:
        left_child_width = answers[node][1]
        for answer in answers:
            if answer[1] >= left_child_width:
                answer[1] += 1
        answers[left_child] = ([child_height, left_child_width])
        q.append(left_child)
    if right_child != -1:
        right_child_width = answers[node][1] + 1
        for answer in answers:
            if answer[1] >= right_child_width:
                answer[1] += 1
        answers[right_child] = ([child_height, right_child_width])
        q.append(right_child)

# output
count_dic = {}
for answer in answers:
    if answer[0] not in count_dic:
        count_dic[answer[0]] = [answer[1]]
    else:
        count_dic[answer[0]].append(answer[1])
count_list = []
for key, value in count_dic.items():
    answer = max(value) - min(value) + 1
    count_list.append([key, answer])
count_list.sort(key=lambda x: (-x[1], x[0]))
print(count_list[0][0], count_list[0][1])
