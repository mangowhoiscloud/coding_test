import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M, V = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ansDFS = []
ansBFS = []

for i in range(M):
    here, there = list(map(int, input().split()))
    graph[here].append(there)
    graph[there].append(here)

for here in range(1, N+1):
    graph[here].sort()

def reset():
    global visited
    visited = [False] * (N+1)

def DFS(here):
    ansDFS.append(here)
    visited[here] = True
    for there in graph[here]:
        if not visited[there]:
            DFS(there)

def BFS(start):
    visited[start] = True
    que = list()
    que.append(start)
    
    while len(que) > 0:
        here = que.pop(0)
        ansBFS.append(here)
        for there in graph[here]:
            if not visited[there]:
                visited[there] = True
                que.append(there)

DFS(V)
reset()
BFS(V)

print(*ansDFS)
print(*ansBFS)