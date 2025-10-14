import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = list(map(int, input().split()))
lessons = list(map(int, input().split()))
maxSize, minSize = 0, 0

for lesson in lessons:
    maxSize += lesson
    minSize = max(lesson, minSize)
    
answer = maxSize

def getCount(mSize):
    count = 1
    size  = mSize
    for lesson in lessons:
        if lesson > size:
            count += 1
            size = mSize - lesson
        else:
            size -= lesson
    return count

def binarySearch(startSize, endSize):
    global answer
    mSize = (endSize + startSize) // 2
    if startSize > endSize:
        answer = startSize
        return
    count = getCount(mSize)
    if   count > M:
        binarySearch(mSize + 1, endSize)
    elif count < M:
        binarySearch(startSize, mSize-1)
    else:
        answer = mSize
        binarySearch(startSize, mSize-1)
        return    

binarySearch(minSize, maxSize)
print(answer)