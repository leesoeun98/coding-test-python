n=int(input())
num=list(map(int, input().split()))
a, b, c, d=list(map(int, input().split()))
#_max는 가장 작은 값으로 초기화, _min은 가장 큰 값으로 초기화
_max=-1e9
_min=1e9
def calc(idx, res, a, b, c, d):
    #재귀함수 끝내는 조건
    global _max, _min
    #idx가 n과 같아지면 최대 최소 비교 후 종료
    if idx==n:
        _max=max(res, _max)
        _min=min(res, _min)
        return
    else:
        if a:
            calc(idx+1, res+num[idx], a-1, b, c, d)
        if b:
            calc(idx+1, res-num[idx], a, b-1, c, d)
        if c:
            calc(idx + 1, res * num[idx], a, b, c-1, d)
        if d:
            calc(idx + 1, int(res / num[idx]), a, b, c, d-1)

calc(1, num[0], a, b, c, d)
print(_max)
print(_min)