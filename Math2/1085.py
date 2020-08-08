x, y, w, h=map(int, input().split())
#굳이 대각선은 고려안해도 됨
print(min(w-x, h-y, x, y))