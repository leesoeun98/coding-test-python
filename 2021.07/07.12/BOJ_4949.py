import sys
while True:
    word=sys.stdin.readline().rstrip()
    if word=='.':
        break
    else:
        stack=[]
        for w in word:
            if w=='[':
                stack.append(w)
            elif w=='(':
                stack.append(w)
            elif w==')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(w)
            elif w==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(w)
        if len(stack)==0:
            print("yes")
        else:
            print("no")