import math

sum = 0
n, m   = list(map(int, input().split()))
array  = [0] + list(map(int, input().split()))
prefix = [0] * (n+1)
modSet = [0] * m

for i in range(1, n+1):
    prefix[i] += (prefix[i-1] % m + array[i] % m) % m

for pre in prefix:
    modSet[pre] += 1

for i in range(0,m):
    modCnt = modSet[i]
    if modCnt == 0:
        sum += modCnt
    if modCnt >= 2:
        sum += modCnt * (modCnt-1) // 2

print(sum)

