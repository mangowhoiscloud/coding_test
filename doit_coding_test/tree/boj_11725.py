import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(0, n+1)]
visited = [False for _ in range(0, n+1)]
parent = [-1 for _ in range(0, n+1)]

for i in range(1, n):
    here, there = map(int, input().split())
    tree[here] .append(there)
    tree[there].append(here)

def dfs(here):
    visited[here] = True
    for there in tree[here]:
        if visited[there]: continue
        parent[there] = here
        dfs(there)

dfs(1)

for pIdx in range(2, n+1):
    print(parent[pIdx])