equ = input()
operator=['/','-','+','*']
def order(x):
    if x=='/' or x=='*':
        return 1
    elif x=='+' or x=='-':
        return 0
stack=[]
for e in equ:
    if e.isdigit():
        print(e, end="")
    else:
        if e in operator:
            while stack and stack[-1] in operator and order(stack[-1])>=order(e):
                print(stack.pop(), end="")
            stack.append(e)
        elif e=='(':
            stack.append(e)
        elif e==')':
            while stack and stack[-1]!='(':
                print(stack.pop(), end="")
            stack.pop()
while stack:
    print(stack.pop(), end="")