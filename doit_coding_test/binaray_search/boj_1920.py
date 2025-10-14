import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
data = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

data = [0] + sorted(data)

def binary(target, startIdx, endIdx):
    mIdx = startIdx + (endIdx-startIdx) // 2
    if startIdx > endIdx:
        print(0)
    elif target == data[mIdx]:
        print(1)        
    elif target > data[mIdx]:
        binary(target, mIdx+1, endIdx)
    else:
        binary(target, startIdx, mIdx-1)
    
for target in targets:
    binary(target, 1, len(data)-1)