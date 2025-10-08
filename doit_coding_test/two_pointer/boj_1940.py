n = int(input())
m = int(input())

material = list(map(int, input().split()))
material.sort()

armor, count = 0, 0
leftIdx, rightIdx = 0, n-1


while leftIdx < rightIdx:
    if material[leftIdx] + material[rightIdx] > m:
        rightIdx -= 1
    elif material[leftIdx] + material[rightIdx] < m:
        leftIdx += 1
    else:
        count += 1
        leftIdx += 1
        rightIdx -= 1
        
print(count)
