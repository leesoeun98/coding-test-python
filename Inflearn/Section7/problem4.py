#이해불가 답안 봄 
t= int(input())
k = int(input())
changeValue=[]
changeN=[]
count=0
for i in range(k):
    v, n = map(int, input().split())
    changeValue.append(v)
    changeN.append(n)
def DFS(depth, sumc):
    global count
    if sumc>t:
        return
    if depth==k:
        if sumc==t:
            count+=1
    else:
        for i in range(changeN[depth]+1):
            DFS(depth+1, sumc+changeValue[depth]*i)
DFS(0,0)
print(count)