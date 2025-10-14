from queue import PriorityQueue
import sys

input  = sys.stdin.readline
output = sys.stdout.writelines 

pq = PriorityQueue()
n = int(input())
ans = 0

for i in range(n):
    pq.put(int(input()))

while pq.qsize() > 1:
    deck = pq.get() + pq.get()
    ans += deck
    pq.put(deck)

print(ans)