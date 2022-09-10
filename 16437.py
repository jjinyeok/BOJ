import sys
n = int(sys.stdin.readline())

tree = {i: [] for i in range(1, n + 1)}
tree_check = {i: [] for i in range(1, n + 1)}
sheeps = [0 for _ in range(n + 1)]
answers = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(2, n + 1):
    type, a, p = sys.stdin.readline().split()
    a, p = int(a), int(p)
    tree[p].append(i)
    tree_check[p].append(i)
    if type == 'S':
        sheeps[i] = a
    elif type == 'W':
        sheeps[i] = a * (-1)

stack = [1]
while stack:
    if tree_check[stack[len(stack) - 1]] == []:
        temp_val = sheeps[stack[len(stack) - 1]]
        for node in tree[stack[len(stack) - 1]]:
            temp_val += answers[node]
        answers[stack[len(stack) - 1]] += max(0, temp_val)
        stack.pop()
    else:
        for node in tree_check[stack[len(stack) - 1]]:
            tree_check[stack[len(stack) - 1]].remove(node)
            answers[stack[len(stack) - 1]] += max(0, answers[node])
            stack.append(node)
            break
print(answers[1])
