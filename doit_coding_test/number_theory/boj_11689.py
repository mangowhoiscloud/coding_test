import sys
import math

input = sys.stdin.readline

n = int(input())
result = n

def getResult():
    global n, result
    for j in range(2, int(math.sqrt(n))+1):
        if n % j == 0:
            result -= result // j
            while n % j == 0:
                n //= j
    if n > 1:
        result -= result//n

getResult()
print(result)