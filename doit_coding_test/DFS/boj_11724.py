import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = 0

for i in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True
    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(neighbour)

for node in range(1, N+1):
    if not visited[node]:
        dfs(node)
        result += 1

print(result)