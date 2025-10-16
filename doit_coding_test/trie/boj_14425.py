n, m = map(int, input().split())
sample = {input().strip() for _ in range(n)}
ret = 0


for _ in range(m):
    word = input().strip()
    if word in sample:
        ret += 1
print(ret)