def Binary(x):
    if x==0:
        return
    else:
        Binary(x//2)
        print(x%2, end="")
Binary(int(input()))