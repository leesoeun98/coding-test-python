n=int(input())
graph=[]
visited=[[0]*n for _ in range(n)]
for i in range(n):
    graph.append(list(list(map(int, input()))))
    #2중for문 입력받기

nums=0 #아파트 수
numlist=[] #아파트 수 저장할 배열
x=[-1,1,0,0] #4방향중 x축
y=[0,0,-1,1] #4방향중 y축

def DFS(i, j, count):
    # graph 전체에서 1을 확인 -> visted에 숫자넣기
    if graph[i][j]==1:
        global nums
        nums+=1
    visited[i][j]=count
    for direction in range(4):
        # 동서남북 인접한 곳에 1이 있는지 확인 -> 재귀호출로 visted에 숫자넣기
        # 인접한 곳에 1 더이상 없으면 다음 전체 graph에서 1 확인
        nearx=i+x[direction]
        neary=j+y[direction]
        if 0<=nearx<n and 0<=neary<n:
            if graph[nearx][neary]==1 and visited[nearx][neary]==0:
                DFS(nearx, neary, count)

count=1
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visited[i][j]==0:
            DFS(i, j, count)
            numlist.append(nums)
            count+=1
            nums=0

#answer
print(len(numlist))
#오름차순 정렬에 주의
for i in sorted(numlist):
    print(i)