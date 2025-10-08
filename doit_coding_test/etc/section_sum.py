n, m  = list(map(int, input().split()))
array = list(map(int, input().split()))
prefix = [0]

for i in range(1, n+1):
    presum = prefix[i-1] + array[i-1]
    prefix.append(presum)

for k in range(0, m):
    i, j = list(map(int,input().split()))
    print(prefix[j] - prefix[i])