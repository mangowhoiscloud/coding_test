from collections import deque

n = int(input())
deq = deque(range(n, 0, -1))

while len(deq) > 1:
    deq.pop()
    bottom = deq.pop()
    deq.appendleft(bottom)

print(deq[-1])