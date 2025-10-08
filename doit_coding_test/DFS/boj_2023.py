import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

prime = [2, 3, 5, 7]

N = int(input())

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True

def dfs(num):
    if len(str(num)) == N:
        print(num)
        return
    for i in range(1, 10, 2):
        nextNum = num*10 + i
        if isPrime(nextNum):
            dfs(nextNum)

for num in prime:
    dfs(num)