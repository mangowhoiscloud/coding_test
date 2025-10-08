from collections import deque
N, L  = list(map(int, input().split()))
array = list(map(int, input().split()))
result = [0] * N
deq = deque()

def addTo(index):
    number = array[index]
    if len(deq) == 0:
        deq.append((index, number))
        return
    right = deq[-1][1]
    while right > number:
        deq.pop()
        if len(deq) == 0:
            break
        right = deq[-1][1]
    deq.append((index, number))

for i in range(N):
    addTo(i)
    if deq[0][0] < i - L + 1:
        deq.popleft()
    result[i] = deq[0][1]

print(*result)