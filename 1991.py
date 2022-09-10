import sys
n = int(sys.stdin.readline())
preorders, inorders, postorders = [], [], []
for _ in range(n):
    parent, child_left, child_right = sys.stdin.readline().split()
    if parent == 'A':
        preorder_answer = (parent + child_left + child_right).replace('.', '')
        inorder_answer = (child_left + parent + child_right).replace('.', '')
        postorder_answer = (child_left + child_right + parent).replace('.', '')
    else:
        preorders.append((parent + child_left + child_right))
        inorders.append((child_left + parent + child_right))
        postorders.append((child_left + child_right + parent))

# preorder
while True:
    check = True
    for alphabet in preorder_answer:
        for preorder in preorders:
            if alphabet == preorder[0]:
                preorder_answer = preorder_answer.replace(alphabet, preorder).replace('.', '')
                preorders.remove(preorder)
                check = False
    if check:
        break

# inorder
while True:
    check = True
    for alphabet in inorder_answer:
        for inorder in inorders:
            if alphabet == inorder[1]:
                inorder_answer = inorder_answer.replace(alphabet, inorder).replace('.', '')
                inorders.remove(inorder)
                check = False
    if check:
        break

# postorder
while True:
    check = True
    for alphabet in postorder_answer:
        for postorder in postorders:
            if alphabet == postorder[2]:
                postorder_answer = postorder_answer.replace(alphabet, postorder).replace('.', '')
                postorders.remove(postorder)
                check = False
    if check:
        break

print(preorder_answer)
print(inorder_answer)
print(postorder_answer)
