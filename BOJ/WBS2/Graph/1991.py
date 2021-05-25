tree={}
# 입력 구현에 약했음 => dict로 받으면 됨
for _ in range(int(input())):
    root, left, right=input().split()
    tree[root]=[left, right]

# left - root - right
def inorder(root):
    if root!='.':
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])

# root - left - right
def preorder(root):
    if root!='.':
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])

# left - right - root
def postorder(root):
    if root!='.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')