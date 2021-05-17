bar = list(input())
stack=[]
total=0
for i in range(len(bar)):
    if bar[i]=='(':
        stack.append(bar[i])
    else:
        stack.pop()
        if bar[i-1]=='(':
            total+=len(stack)
        else:
            total+=1
print(total)