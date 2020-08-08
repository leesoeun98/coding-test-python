import math
a, b, v=map(int, input().split())
#ababab.....a 무조건 a로 시작해서 a로 끝나므로
#첫 번째 a제외하면 a와 b 짝지을 수 있음
print(int(math.ceil((v-a)/(a-b)))+1)