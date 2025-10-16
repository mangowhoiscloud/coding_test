import math

min, max = list(map(int, input().split()))
isPow = [False for i in range(0, max-min+1)]

def isPrime():
    for i in range(2, int(math.sqrt(max) + 1)):
        pow = i * i
        start_idx = int(min/pow)
        if min % pow != 0:
            start_idx += 1
        for j in range(start_idx, int(max/pow)+1):
            isPow[int((j*pow) - min)] = True

count = 0

isPrime()

for num in range(0, max-min+1):
    if not isPow[num]:
        count += 1

print(count)