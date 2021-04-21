n = int(input())
num=list(map(int, input().split()))
total=sum(num)
def DFS(depth, sumnum):
    if depth==n:
        if total-sumnum==sumnum:
            print("YES")
            exit(0)
        return
    else:
        #넣고
        DFS(depth+1, sumnum+num[depth])
        #안넣고
        DFS(depth+1, sumnum)
DFS(0,0)
print("NO")
