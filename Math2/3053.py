import math
#택시기하학에서 가장 중요한 것은 원이 정사각형 모양이라는 점
#즉, 택시기하학에선 원의 넓이가 곧 2r^2이다.
r=int(input())
u=math.pi*r*r
m=2.000000*r*r
print("%.6f" %round(u, 6))
print("%.6f" %m)