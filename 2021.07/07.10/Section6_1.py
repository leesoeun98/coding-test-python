n = int(input())
def dfs(n):
    if n>0:
        dfs(n//2)
        print(n%2, end="")
dfs(n)