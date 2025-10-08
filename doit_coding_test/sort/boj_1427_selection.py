# O(N^2)
array = [int(_) for _ in str(input())]
n = len(array)

for i in range(n):
    max, maxIdx = array[i], i
    for j in range(i+1, n):
        if max < array[j]:
            max, maxIdx = array[j], j
    array[i], array[maxIdx] = array[maxIdx], array[i]
            

print(*array,sep='')