#1차 시도 답안 봄
bar=input()
stack=[]
total=0
for i in range(len(bar)):
    if bar[i]=='(':
        stack.append(bar[i])
    else:
        stack.pop()
        if bar[i-1]=='(':
            total+=len(stack)
        #))면 막대 1개만 끝났으므로 +1
        else:
            total+=1
print(total)
