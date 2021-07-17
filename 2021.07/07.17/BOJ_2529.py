n = int(input())
temp = input()
relation=[]
for r in temp:
    if r=='>' or r=='<':
        relation.append(r)
visited=[0]*10
ans=[]

def check(i, j, k):
    if k=='>':
        return i>j
    else:
        return i<j

def dfs(depth, s):
    if depth==n+1:
        ans.append(s)
        return
    for i in range(10):
        if visited[i]==0:
            if depth==0 or check(s[-1], str(i), relation[depth-1]):
                visited[i]=1
                dfs(depth+1, s+str(i))
                visited[i]=0

dfs(0, "")
print(ans[-1])
print(ans[0])