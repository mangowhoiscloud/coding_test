import sys
import math

input = sys.stdin.readline

M, N = list(map(int, input().split()))
isPrime = [True] * (N+1)

def setPrime():
    global isPrime
    isPrime[1] = False
    for num in range(2, int(math.sqrt(N))+1):
        if not isPrime[num]:
            continue
        for j in range(num * 2, N+1, num):
            isPrime[j] = False
def printPrime():
    global isPrime, M, N
    for num in range(M, N+1):
        if isPrime[num]:
            print(num)

setPrime()
printPrime()