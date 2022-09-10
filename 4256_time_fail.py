# 모든 경우의 tree를 preorder와 inorder를 확인했기 때문에 시간이 초과되었다.

import sys, copy
from collections import deque

def preorder(tree, value, answer):
    answer.append(value)
    if tree[value][0] != -1:
        preorder(tree, tree[value][0], answer)
    if tree[value][1] != -1:
        preorder(tree, tree[value][1], answer)
    return answer

def inorder(tree, value, answer):
    if tree[value][0] != -1:
        inorder(tree, tree[value][0], answer)
    answer.append(value)
    if tree[value][1] != -1:
        inorder(tree, tree[value][1], answer)
    return answer

def postorder(tree, value, answer):
    if tree[value][0] != -1:
        postorder(tree, tree[value][0], answer)
    if tree[value][1] != -1:
        postorder(tree, tree[value][1], answer)
    answer.append(value)
    return answer

def make_tree(tree, n, index, preorder_list, inorder_list, root):
    if len(tree.keys()) == n:
        if preorder(tree, root, []) == preorder_list and inorder(tree, root, []) == inorder_list:
            print(' '.join(map(str, postorder(tree, root, []))))
            return tree
    elif len(tree.keys()) < n:
        for key, value in tree.items():
            if value[0] == -1:
                temp_tree = copy.deepcopy(tree)
                temp_tree[preorder_list[index]] = [-1, -1]
                temp_tree[key][0] = preorder_list[index]
                make_tree(temp_tree, n, index + 1, preorder_list, inorder_list, root)
            if value[1] == -1:
                temp_tree = copy.deepcopy(tree)
                temp_tree[preorder_list[index]] = [-1, -1]
                temp_tree[key][1] = preorder_list[index]
                make_tree(temp_tree, n, index + 1, preorder_list, inorder_list, root)

# input
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    preorder_list = list(map(int, sys.stdin.readline().split()))
    inorder_list = list(map(int, sys.stdin.readline().split()))
    root = preorder_list[0]

    tree = {root: [-1, -1]}
    a =  make_tree(tree=tree, n=n, index=1, preorder_list=preorder_list, inorder_list=inorder_list, root=root)
    