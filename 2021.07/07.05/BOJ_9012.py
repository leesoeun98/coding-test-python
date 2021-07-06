for _ in range(int(input())):
    ps = list(input())
    stack=[]
    flag=True
    for p in ps:
        if p=='(':
            stack.append(p)
        elif p==')' and stack:
            stack.pop()
        elif p==')' and not stack:
            flag=False
            break
    if len(stack)!=0:
        flag=False
    if flag:
        print("YES")
    else:
        print("NO")