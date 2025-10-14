import sys
import math

input = sys.stdin.readline
isPrime = [True for _ in range(0, 10**7+1)]
N = int(input())

def setPrime():
    isPrime[1] = False
    for i in range(2, int(math.sqrt(len(isPrime)))+1):
        if not isPrime[i]:
            continue
        for j in range(i+i, len(isPrime), i):
            isPrime[j] = False

def isPallin(num):
    strNum = list(str(num))
    s, e = 0, len(strNum) - 1
    while s < e:
        if strNum[s] != strNum[e]:
            return False
        s += 1
        e -= 1
    return True
    

def getPallin():
    for num in range(N, len(isPrime)):
        if not isPrime[num]:
            continue
        if isPallin(num):
            print(num)
            return

setPrime()
getPallin()