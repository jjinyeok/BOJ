import sys
from collections import deque

def postorder(tree, value, answer):
    if tree[value][0] != -1:
        postorder(tree, tree[value][0], answer)
    if tree[value][1] != -1:
        postorder(tree, tree[value][1], answer)
    answer.append(value)
    return answer

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    
    root = preorder[0]
    tree = {root: [-1, -1]}
    q = deque()
    q.append([preorder, inorder, root])

    while q:
        preorder, inorder, value = q.popleft()
        index = inorder.index(value)

        left_inorder, right_inorder = inorder[: index], inorder[index + 1 :]
        left_preorder, right_preorder = preorder[1 : len(left_inorder) + 1], preorder[len(left_inorder) + 1 :]
        
        if len(left_preorder) > 0:
            left_node = left_preorder[0]
            tree[value][0] = left_node
            tree[left_node] = [-1, -1]
            if len(left_preorder) > 1:
                q.append([left_preorder, left_inorder, left_node])
        if len(right_preorder) > 0:
            right_node = right_preorder[0]
            tree[value][1] = right_node
            tree[right_node] = [-1, -1]
            if len(right_preorder) > 1:
                q.append([right_preorder, right_inorder, right_node])

    answer = postorder(tree, root, [])
    print(' '.join(map(str, answer)))
