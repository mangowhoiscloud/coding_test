from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline

pq = PriorityQueue()
n = int(input())

for i in range(n):
    x = int(input())
    if x == 0:
        if pq.empty():
            print('0\n')
        else:
            print(str(pq.get()[1])+'\n')
    else:
        pq.put((abs(x), x))