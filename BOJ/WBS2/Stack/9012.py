for _ in range(int(input())):
    ps = list(input())
    stack = []
    # (면 append, )면 pop을 하되 pop할게 없으면 no
    # 다했는데 stack에 남아있으면 no
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append(ps[i])
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")
"""
for _ in range(int(input())):
    stack=[]
    bracket = list(input())
    for i in range(len(bracket)):
        if bracket[i]=='(':
            stack.append(bracket[i])
        elif bracket[i]==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(bracket[i])
    if len(stack)!=0:
        print("NO")
    else:
        print("YES")


"""