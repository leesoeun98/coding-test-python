bar = input()
stack=[]
length=0
for i in range(len(bar)):
    if bar[i]=='(':
        stack.append(bar[i])
    else:
        stack.pop()
        if i>1 and bar[i-1]=='(':
            length+=len(stack)
        elif i>1 and bar[i-1]==')':
            length+=1
print(length)