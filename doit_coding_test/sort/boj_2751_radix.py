import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]

neg = [-v for v in array if v < 0]   
pos = [ v for v in array if v >= 0]

def radix_nonneg(a):
    if not a: return a
    m = max(a)
    exp = 1
    while m // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in a:
            buckets[(x // exp) % 10].append(x)
        a = [v for b in buckets for v in b]
        exp *= 10
    return a

neg_sorted = radix_nonneg(neg)       
pos_sorted = radix_nonneg(pos)       

array = [-v for v in reversed(neg_sorted)] + pos_sorted
print(*array)
