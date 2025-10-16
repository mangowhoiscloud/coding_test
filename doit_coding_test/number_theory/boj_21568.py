import math

a, b, c = list(map(int, input().split()))
x, y = 1, 0

def expandGCD(a,b):
    if b == 0:
        return 1, 0
    q = a // b
    v = expandGCD(b, a%b)
    return v[1], v[0] - v[1] * q

mgcd = math.gcd(a, b)

if c % mgcd != 0:
    print(-1)
else:
    mok = int(c / mgcd)
    ret = expandGCD(a,b)
    print(ret[0] * mok, end = ' ')
    print(ret[1] * mok)    