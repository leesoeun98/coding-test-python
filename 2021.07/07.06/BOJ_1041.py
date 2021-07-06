n = int(input())
nums= list(map(int, input().split()))

# 블록의 최소 숫자를 계산하는데서 틀림
sumList=[]
sumList.append((min(nums[0], nums[5])))
sumList.append((min(nums[1], nums[4])))
sumList.append((min(nums[2], nums[3])))
sumList.sort()

res=0
# 블록 총 개수당 면 몇개인지를 알아야 함
if n==1:
    nums.sort()
    for i in range(5):
        res+=nums[i]
else:
    blocks=[0,(n-2)*(n-2)+(n-2)*(n-1)*4, 4*(n-1)+n*n-4-(n-2)*(n-2), 4]
    blocknums=[0,sumList[0], sumList[0]+sumList[1], sumList[0]+sumList[1]+sumList[2]]
    for i in range(len(blocks)):
        res+=blocks[i]*blocknums[i]

print(res)