code = list(map(int, input()))
n = len(code)
code.insert(n, -1)
res = [0] * (100)
count = 0


def DFS(depth, position):
    global count
    if depth == n:
        count += 1
        for j in range(position):
            print(chr(res[j] + 64), end="")
        print()
        return
    else:
        for i in range(1, 27):
            # 알파벳 26개의 가지가 나감. 각 code[depth] 글자가 i에 해당하는지 확인
            # 한글자
            if i < 10 and code[depth] == i:
                res[position] = i
                DFS(depth + 1, position + 1)
            # 두글자
            elif i >= 10 and code[depth] == i // 10 and code[depth + 1] == i % 10:
                res[position] = i
                DFS(depth + 2, position + 1)


DFS(0, 0)
print(count)

"""
code=list(map(int, str(input())))
ans=[]
count=0
def dfs(depth, res):
    global count
    if depth==len(code):
        ans.append(''.join(res))
        count+=1
        return
    else:
        for i in range(1, 27):
            # 한 자리
            if i<10 and code[depth]==i:
                dfs(depth+1, res+[chr(ord('A')-1+i)])
            # 두 자리
            elif depth<len(code)-1:
                if 10<=i<27 and code[depth]==i//10 and code[depth+1]==i%10:
                    dfs(depth+2, res+[chr(ord('A')-1+i)])
dfs(0,[])
print(ans)
print(count)"""