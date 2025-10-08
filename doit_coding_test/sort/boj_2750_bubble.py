# O(N^2)
n = int(input())
array = list()

def bubbleSort():
    n = len(array)
    for i in range(n):
        for j in range(0, n-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

for i in range(n):
    x = int(input())
    array.append(x)

bubbleSort()

print(*array, sep="\n")