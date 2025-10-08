maxNum = 10000
n = int(input())
cntList = [0] * (maxNum+1)

for i in range(n):
    num = int(input())
    cntList[num] += 1

for num in range(1, maxNum+1):
    cnt = cntList[num]
    for i in range(0, cnt):
        print(num)