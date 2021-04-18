#숫자면 print
#연산자면 자신과 stack 비교시 우선순위 높거나 같을때까지 pop 아니면 push
#(면 push
#)면 (때까지 pop
def Priority(x):
    if x=='-' or x=='+':
        return 0
    elif x=='*' or x=='/':
        return 1
eq=input()
res=""
operator=['-','+','/','*']
stack=[]
for e in eq:
    if e.isdigit():
        res+=e
    else:
        if e in operator:
            while stack and stack[-1] in operator and Priority(stack[-1])>=Priority(e):
                res+=stack.pop()
            stack.append(e)
        elif e=='(':
            stack.append(e)
        elif e==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)
