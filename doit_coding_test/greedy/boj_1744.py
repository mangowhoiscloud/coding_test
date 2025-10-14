import sys
from queue import PriorityQueue

input = sys.stdin.readline
positiveQue = PriorityQueue()
negativeQue = PriorityQueue()
ans = 0
n = int(input())

for _ in range(n):
    number = int(input())
    if number <= 0:
        negativeQue.put(number)
    elif number == 1:
        ans += 1
    else:
        positiveQue.put(-number)

def combine(pq, offset):
    ret = 0
    while not pq.empty():
        if pq.qsize() > 1:
            ret += (pq.get() * pq.get())
        else:
            ret += pq.get() * offset
    return ret

ans += combine(negativeQue,1) + combine(positiveQue, -1)
print(ans)