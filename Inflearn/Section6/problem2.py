def preorder(v):
    if v>7:
        return
    else:
        #root
        print(v, end=" ")
        #left
        preorder(v*2)
        #right
        preorder(v*2+1)
def inorder(v):
    if v>7:
        return
    else:
        #left
        inorder(v*2)
        #root
        print(v, end=" ")
        #right
        inorder(v*2+1)
def postorder(v):
    if v>7:
        return
    else:
        #left
        inorder(v*2)
        #right
        inorder(v*2+1)
        #root
        print(v, end=" ")

if __name__=="__main__":
    preorder(1)
    print()
    inorder(1)
    print()
    postorder(1)