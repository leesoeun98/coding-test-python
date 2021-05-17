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
