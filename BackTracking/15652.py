#dfs 쓰는 문제
n, m=map(int, input().split())
#결과 배열
out=[0]*m
def solve(depth, n, m, next):
    #재귀 벗어나는 조건쓰기
     if depth==m:
         #m의 길이만큼 답 출력
         for i in range(m):
             print(out[i], end=" ")
         print()
         return
     #out[1]의 i가 next부터 돌아야함
     for i in range(next, n+1):
             out[depth]=i
             solve(depth+1, n, m, i)

solve(0,n,m, 1)