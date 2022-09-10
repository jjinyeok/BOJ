# 모든 경우의 tree를 만들어 queue에 집어넣었기 때문에 메모리가 초과되었다.

import sys, copy
from collections import deque

def inorder_func(tree, value, answer):
    if tree[value][0] != -1:
        inorder_func(tree, tree[value][0], answer)
    answer.append(value)
    if tree[value][1] != -1:
        inorder_func(tree, tree[value][1], answer)
    return answer

def postorder_func(tree, value, answer):
    if tree[value][0] != -1:
        postorder_func(tree, tree[value][0], answer)
    if tree[value][1] != -1:
        postorder_func(tree, tree[value][1], answer)
    answer.append(value)
    return answer

# input
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    root = preorder[0]

# find tree by preorder and inorder
    q = deque()
    q.append([{preorder[0]: [-1, -1]}, 0])
    while q:
        tree, index = q.popleft()
        for key, value in tree.items():
            left_node, right_node = value
            if index != n - 1:
                if left_node == -1 and preorder[index + 1] not in tree and right_node == -1:
                    temp_tree = copy.deepcopy(tree)
                    temp_tree[key][0] = preorder[index + 1]
                    temp_tree[preorder[index + 1]] = [-1, -1]
                    
                    # find tree success
                    if index == n - 2:
                        inorder_value = inorder_func(temp_tree, root, [])
                        if inorder_value == inorder:
                            answer_tree = tree
                            break
                    
                    else: q.append([temp_tree, index + 1])
                    
                if right_node == -1 and preorder[index + 1] not in tree:
                    temp_tree = copy.deepcopy(tree)
                    temp_tree[key][1] = preorder[index + 1]
                    temp_tree[preorder[index + 1]] = [-1, -1]

                    # find tree success
                    if index == n - 2:
                        inorder_value = inorder_func(temp_tree, root, [])
                        if inorder_value == inorder:
                            answer_tree = tree
                            break
                    
                    else: q.append([temp_tree, index + 1])

    answer = postorder_func(answer_tree, root, [])
    print(' '.join(list(map(str, answer))))
