import sys
from queue import PriorityQueue

input = sys.stdin.readline
n = int(input())
pq = PriorityQueue()
ans, time = 0, 0

for _ in range(n):
    startTime, endTime = list(map(int, input().split()))
    pq.put((endTime, startTime))

while not pq.empty():
    meeting = pq.get()
    if meeting[1] < time:
        continue
    ans += 1
    time = meeting[0]

print(ans)
