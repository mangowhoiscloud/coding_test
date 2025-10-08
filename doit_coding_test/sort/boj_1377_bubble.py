# O(N^2)
import sys
input = sys.stdin.readline

n = int(input())
result = 0
array = list()

for i in range(n):
    x = int(input())
    array.append((x, i))

sortedArray = sorted(array)

for i in range(n):
    count = sortedArray[i][1] - i + 1
    if result < count:
        result = count

print(result)