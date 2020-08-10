#dfs 쓰는 문제
n, m=map(int, input().split())
#결과 배열
out=[0]*m
def solve(depth, n, m):
    #재귀 벗어나는 조건쓰기
     if depth==m:
         #m의 길이만큼 답 출력
         for i in out:
             print(i, end=" ")
         print()
         return
     for i in range(1, n+1):
             out[depth]=i
             solve(depth+1, n, m)

solve(0,n,m)