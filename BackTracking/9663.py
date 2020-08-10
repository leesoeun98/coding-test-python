n=int(input())
res=0
col=[0]*(n+1)
def ispossible(c):
    for i in range(1, c):
        #같은 열이면 false
        if(col[i]==col[c]):
            return False
        #같은 대각선이면 false
        if abs(col[c]-col[i])==abs(c-i):
            return False
    #나머지 경우에 true
    return True
def nqueen(row):
    global res
    #행 넘어가면 말단에서 res+=1
    if row>n:
        res+=1
    #말단 행이 아니면 row+1로 nqueen 재귀 호출할거임 -> 단, 백트래킹 가지치기해서 유망한 노드에서만
    else:
        #한 행에 대해서 모든 열을 검사
        for i in range(1, n+1):
            #현재 위치 저장 
            col[row]=i
            print(col)
            #해당 행에서 해당 좌표 통과시 유망하므로 다음 행으로 이동
            if ispossible(row):
                nqueen(row+1)
nqueen(1)
print(res)

