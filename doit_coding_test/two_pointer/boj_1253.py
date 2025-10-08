n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
count = 0

for i in range(n):
    key = numbers[i]
    leftIdx, rightIdx = 0, n-1
    while leftIdx < rightIdx:
        if leftIdx == i:
            leftIdx += 1
            continue
        elif rightIdx == i:
            rightIdx -= 1
            continue
        if numbers[leftIdx] + numbers[rightIdx] < key:
            leftIdx += 1
        elif numbers[leftIdx] + numbers[rightIdx] > key:
            rightIdx -= 1
        else:
            count += 1
            break
print(count)