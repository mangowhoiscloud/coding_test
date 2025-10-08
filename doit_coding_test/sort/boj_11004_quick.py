# O(nlogn) ~ O(n)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))

def swap(i, j):
    global array
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def quickSort(startIdx, endIdx, k):
    global array
    if startIdx < endIdx:
        pivot = partition(startIdx, endIdx)
        if pivot == k:
            return
        elif k < pivot:
            quickSort(startIdx, pivot - 1, k)
        else:
            quickSort(pivot+1, endIdx, k)
            

def partition(startIdx, endIdx):
    global array

    if startIdx + 1 == endIdx:
        if array[startIdx] > array[endIdx]:
            swap(startIdx, endIdx)
        return endIdx
    mIdx = (startIdx+endIdx) // 2
    swap(startIdx, mIdx)
    pivot = array[startIdx]
    i = startIdx + 1
    j = endIdx
    while i <= j:
        while pivot < array[j] and j > 0:
            j = j - 1
        while pivot > array[i] and i < len(array)-1:
            i = i + 1
        if i <= j:
            swap(i,j)
            i += 1
            j -= 1
    array[startIdx] = array[j]
    array[j] = pivot
    return j

quickSort(0, n-1, k-1)
print(array[k-1])