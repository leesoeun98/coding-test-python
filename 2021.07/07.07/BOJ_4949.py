import sys
while True:
    line = sys.stdin.readline().rstrip()
    stack=[]
    flag=True
    if line=='.':
        exit(0)
    else:
        for l in line:
            if l=='(':
                stack.append(l)
            elif l=='[':
                stack.append(l)
            elif l==')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    flag=False
                    break
            elif l==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    flag=False
                    break
        if len(stack)!=0:
            flag=False
        if flag:
            print("yes")
        else:
            print("no")
