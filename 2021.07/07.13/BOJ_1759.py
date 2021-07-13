l, c = map(int, input().split())
code=list(input().split())
code.sort()
res=[' ']*l
lst=['a','e','i','o','u']

def check(word):
    cnt1=0
    cnt2=0
    for w in word:
        if w in lst:
            cnt1+=1
        else:
            cnt2+=1
    if cnt1>=1 and cnt2>=2:
        return True
    else:
        return False
ans=set()
def dfs(depth, start):
    if depth==l:
        if check(''.join(res))==True:
            ans.add(''.join(res))
        return
    for i in range(start, len(code)):
        res[depth]=code[i]
        dfs(depth+1, i+1)

dfs(0, 0)
answer=list(ans)
answer.sort()
for a in answer:
    print(a)