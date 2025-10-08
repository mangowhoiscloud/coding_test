# O(N^2)
n = int(input())
time  = list(map(int, input().split()))
spend = list([0] * n)
answer = 0

for i in range(1, n):
    s, sIdx = time[i], i
    for sIdx in range(i-1, -1, -1):
        if time[sIdx] < s:
            sIdx = sIdx+1
            break
    for j in range(i, sIdx, -1):
        time[j] = time[j-1]
    time[sIdx] = s

spend[0] = time[0]

for i in range(1, n):
    spend[i] = spend[i-1] + time[i]        

for i in range(n):
    answer += spend[i]

print(answer)