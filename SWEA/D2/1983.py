for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    total = []
    alphabet = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    for i in range(n):
        m, f, a = map(int, input().split())
        total.append((m * 0.35 + f * 0.45 + a * 0.2, i + 1))
    total.sort(key=lambda x: (-x[0]))
    rank=0
    for i in range(n):
        if total[i][1]==k:
            rank=i
            break
    res = int(rank / n*10)
    print("#"+str(t)+" "+alphabet[res])
