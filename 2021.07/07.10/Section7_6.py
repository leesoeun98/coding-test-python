code=list(map(int, input()))
cnt=0
def dfs(depth, res):
    global cnt
    if depth==len(code):
        print(''.join(res))
        cnt+=1
        return
    else:
        for i in range(1, 26):
            if 0<code[depth]<10 and code[depth]==i:
                dfs(depth+1, res+[chr(code[depth]-1+ord('A'))])
            elif depth<len(code)-1:
                two = int(''.join(str(code[depth]) + str(code[depth + 1])))
                if 10<=two<27 and two==i :
                    dfs(depth+2, res+[chr(two-1+ord('A'))])
dfs(0, [])
print(cnt)