# 답지 봐도 이해안감...답도 안나옴...
code = input()
decr = set()
#out of index 방지
code.insert(len(code), -1)
res=[0]*(len(code)+3)
count=0
def DFS(depth, p):
    global count
    if depth == len(code):
        count+=1
        for j in range(p):
            print(chr(res[j]+64), end="")
        print()
        return
    else:
        for i in range(1, 27):
            if code[depth]==i:
                res[p]=i
                DFS(depth+1, p+1)
            elif i>=10 and code[depth]==i//10 and code[depth+1]==i%10:
                res[p]=i
                DFS(depth+2, p+1)
DFS(0, 0)
print(count)