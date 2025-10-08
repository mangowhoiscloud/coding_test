n = int(input())
leftIdx, rightIdx= 1, 1
sum, count = 1, 0

while rightIdx <= n:
    if sum == n:
        count += 1
    if sum <= n:
        rightIdx += 1
        sum += rightIdx
    else:
        sum -= leftIdx 
        leftIdx += 1

print(count)