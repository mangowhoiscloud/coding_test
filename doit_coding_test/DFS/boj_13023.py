import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

graph = [[] for _ in range(N)]
visited = [False] * N
result = False

for i in range(M):
    here, there = list(map(int, input().split()))
    graph[here] .append(there)
    graph[there].append(here)

def dfs(here, depth):
    if depth == 5:
        print(1)
        exit(0)
    visited[here] = True
    for there in graph[here]:
        if not visited[there]:
            dfs(there, depth+1)
    visited[here] = False

for here in range(N):
    dfs(here, 1)
print(0)