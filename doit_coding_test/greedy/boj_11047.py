wallet = []
n, k = list(map(int, input().split()))
ans, endIdx = 0, 0

for idx in range(n):
    coin = int(input())
    wallet.append(coin)
    if coin <= k:
        endIdx = max(endIdx, idx)

for wIdx in range(endIdx, -1, -1):
    ans += k // wallet[wIdx]
    k = k % wallet[wIdx]
    if k == 0: break

print(ans)