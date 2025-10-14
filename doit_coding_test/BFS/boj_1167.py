import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    info = list(map(int, input().split()))
    here = info[0]
    for i in range(1, len(info)-1, 2):
        there, cost = info[i], info[i+1]
        graph[here].append((there, cost))
        graph[there].append((here, cost))

def BFS(start):
    maxDis = 0
    target = start
    que = list()
    visited = [False] * (v+1)
    distance = [0] * (v+1)
    que.append(start)
    visited[start] = True
    while len(que) > 0:
        here = que.pop(0)
        for there, cost in graph[here]:
            if visited[there]: continue
            distance[there] = distance[here] + cost
            if maxDis < distance[there]:
                maxDis = distance[there]
                target = there
            que.append(there)
            visited[there] = True
    return target, distance[target]

target = BFS(1)[0]
print(BFS(target)[1])