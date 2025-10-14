import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000)

N = int(input())
K = int(input())

answer = 0

def getCount(target):
    ret = 0
    for number in range(1, N+1):
        ret += min(target // number, N)
    return ret

def binarySearch(start, end):
    global answer
    if start > end:
        return
    m = (start + end) // 2
    if getCount(m) < K:
        binarySearch(m+1, end)
    else:
        answer = m
        binarySearch(start, m-1)


binarySearch(1, min(10**9, N**2))
print(answer)