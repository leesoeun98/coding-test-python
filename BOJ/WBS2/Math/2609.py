def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


a, b = map(int, input().split())
print(gcd(a, b))
print("%d" % (a * b / gcd(a, b)))

"""
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)

x, y = map(int, input().split())
print(gcd(x, y))
print(lcm(x, y))"""