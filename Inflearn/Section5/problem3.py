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

"""
#피연산자면 그대로 출력
#연산자이면 연산자 우선순위 높은게 먼저.. stack에 있는거랑 자기자신이랑 비교해서
#자기자신이 더 크면 그대로 push
#자기자신이 더 작으면 stack의 연산자가 더 작아질때까지 pop
#(면 push
#)면 (까지 pop

eq=input()
stack=[]
res=""
operator=['/','-','+','*']
def priority(x):
    if x=='/' or x=='*':
        return 1
    elif x=='-' or x=='+':
        return 0

for e in eq:
    if e.isdigit():
        res+=e
    else:
        if e=='(':
            stack.append(e)
        elif e==')':
            while stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] in operator and priority(stack[-1])>=priority(e):
                res+=stack.pop()
            stack.append(e)
while stack:
    res+=stack.pop()
print(res)
"""