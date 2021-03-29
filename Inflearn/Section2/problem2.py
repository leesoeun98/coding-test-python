for _ in range(int(input())):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    answer = sorted(num[s - 1:e])
    print(answer[k-1])

"""
# slice없이
t = int(input())
for _ in range(t):
  n, s, e, k=map(int, input().split())
  num=list(map(int, input().split()))
  answer=[0 for i in range(e-s+1)]
  idx=0
  for i in range(s-1, e):
    answer[idx]=num[i]
    idx+=1
  answer=sorted(answer)
  print(answer)
  """