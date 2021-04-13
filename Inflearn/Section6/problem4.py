n = int(input())
num=list(map(int, input().split()))
def DFS(depth, firstsum):
    if depth==n:
        if firstsum==sum(num)-firstsum:
            print("YES")
            exit(0)
        return
    else:
        #해당 index 넣은거
        DFS(depth+1, firstsum+num[depth])
        #해당 index 안넣은거
        DFS(depth+1, firstsum)

DFS(0, 0)
print("NO")