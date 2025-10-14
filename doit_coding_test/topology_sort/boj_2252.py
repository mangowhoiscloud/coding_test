import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
ans = []

que = list()

for _ in range(m):
    A, B = list(map(int, input().split()))
    graph[A].append(B)
    indegree[B] += 1

for i in range(1, len(indegree)):
    if indegree[i] == 0:
        que.append(i)

while len(que) > 0:
    here = que.pop(0)
    ans.append(here)
    for there in graph[here]:
        indegree[there] -= 1
        if indegree[there] == 0:
            que.append(there)

print(*ans)