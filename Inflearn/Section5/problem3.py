# 중위 -> 후기
# 1. 피연산자는 바로 출력
# 2. 연산자는 stack의 top보다 우선순위 높거나 같은 것은 pop
# 2. stack의 top보다 우선순위 작은 연산자는 push
# 3. ( 는 무조건 스택에 넣음
# 4. ) 는 (를 만날때까지 스태에서 pop

#1차 시도 답안봄
equation = input()
stack = []
answer = ""
for e in equation:
    if e.isdigit():
        answer += e
    else:
        if e == '(':
            stack.append(e)
        elif e == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()  # ) 제거
        elif e == '+' or e == '-':
            # 가장 낮은 순위 만날때까지 pop
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(e)
        elif e == '*' or e == '/':
            stack.append(e)
while stack:
    answer+=stack.pop()
print(answer)

"""
# 중위 -> 후기
# 1. 피연산자는 바로 출력
# 2. 연산자는 자신보다 우선순위 높거나 같은 것은 pop
# 2. 이후 push
# 3. ( 는 무조건 스택에 넣음
# 4. ) 는 (를 만날때까지 스태에서 pop
def Priority(x):
    if x == '+' or x == '-':
        return 0
    elif x == '*' or x == '/':
        return 1


eq = input()
stack = []
operator = ['-', '+', '*', '/']
for e in eq:
    if e.isdigit():
        print(e, end="")
    elif e in operator:
        while stack and stack[-1] in operator and Priority(e) <= Priority(stack[-1]):
            print(stack.pop(), end="")
        stack.append(e)
    elif e == '(':
        stack.append(e)
    elif e == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end="")
        stack.pop()  # (제거

while stack:
    print(stack.pop(), end="")
"""

"""
#숫자는 print
#연산자이면 자신과 stack비교해서 우선순위 높은거부터 pop
#=> 우선순위 낮으면 일단 stack에 push 높으면 pop
#(면 push
#)면 (나올때까지 pop
eq=input()
stack=[]
res=""
operator=['/','*','-','+']
def getPriority(x):
    if x=='/' or x=='*':
        return 1
    elif x=='-' or x=='+':
        return 0
for e in eq:
    if e.isdigit():
        res+=e
    else:
        if e in operator:
            while stack and stack[-1] in operator and getPriority(stack[-1])>=getPriority(e):
                res+=stack.pop()
            stack.append(e)
        elif e==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
        elif e=='(':
            stack.append(e)
while stack:
    res+=stack.pop()
print(res)
"""