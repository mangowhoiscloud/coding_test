import sys
import math

input = sys.stdin.readline

A, B = list(map(int, input().split()))

isPrime = [True] * (10**7+1)
ans = 0

def setPrime():
    global A,B,isPrime,ans
    isPrime[1] = False
    for i in range(2, int(math.sqrt(len(isPrime)))+1):
        if not isPrime[i]:
            continue
        for j in range(i + i, len(isPrime), i):
            isPrime[j] = False

def almostPrime():
    global A, B, ans
    for num in range(2, len(isPrime)):
        if not isPrime[num]: continue
        almost = num
        while num <= B / almost:
            if num >= A / almost:
                ans += 1
            almost *= num

setPrime()
almostPrime()
print(ans)