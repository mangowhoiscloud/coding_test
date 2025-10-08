n = int(input())
array = [0] + list(map(int, input().split()))
tmp = [0] * (n+1)
answer = 0


def mergeSort(startIdx, endIdx):
    global array, tmp, answer
    if endIdx - startIdx < 1: return
    mIdx = startIdx + (endIdx-startIdx) // 2 
    mergeSort(startIdx, mIdx)
    mergeSort(mIdx+1, endIdx)
    for i in range(startIdx, endIdx+1):
        tmp[i] = array[i]
    k = startIdx
    leftIdx = startIdx
    rightIdx = mIdx + 1
    
    while leftIdx <= mIdx and rightIdx <= endIdx:
        if tmp[leftIdx] > tmp[rightIdx]:
            array[k] = tmp[rightIdx]
            answer += rightIdx - k
            k += 1
            rightIdx += 1
        else:
            array[k] = tmp[leftIdx]
            k += 1
            leftIdx += 1
    
    while leftIdx <= mIdx:
        array[k] = tmp[leftIdx]
        k += 1
        leftIdx += 1
    while rightIdx <= endIdx:
        array[k] = tmp[rightIdx]
        k += 1
        rightIdx += 1

mergeSort(1, n)
print(answer)