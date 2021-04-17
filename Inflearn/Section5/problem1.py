#1차 시도 답안 봄
num, rmcnt=map(int, input().split())
nums=list(map(int, str(num)))
stack=[]
# 숫자를 제거해서 가장 큰 수를 만드려면, 그냥 가장 큰 숫자들만 남겨야 함
# 즉, stack의 값과 비교해서 더 큰걸 남기는 것.
for n in nums:
    while stack and rmcnt>0 and stack[-1]<n:
        stack.pop()
        rmcnt-=1
    stack.append(n)
#for문 다 돌았는데도 rmcnt 남아있으면 남은 만큼 그대로 갖다붙이기
if rmcnt!=0:
    stack=stack[:-rmcnt]
#list =>str => join
res=''.join(map(str, stack))
print(res)