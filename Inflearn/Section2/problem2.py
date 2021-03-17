for _ in range(int(input())):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    answer = sorted(num[s - 1:e])
    print(answer[k-1])
