import sys
import math
input = sys.stdin.readline

n = int(input())
graph = [list() for _ in range(n)]
masses = [0 for _ in range(n)]
visited = [False for _ in range(n)]

lcm = 1

def calLCM(a,b):
    return a*b // math.gcd(a,b)

def dfs(here):
    visited[here] = True
    for there, p, q in graph[here]:
        if visited[there]: continue
        masses[there] = masses[here] * q//p
        dfs(there)

for _ in range(n-1):
    a,b,p,q = map(int, input().split())
    graph[a].append([b, p, q])
    graph[b].append([a, q, p])
    lcm *= calLCM(p,q)

masses[0] = lcm
dfs(0)
mgcd = masses[0]

for i in range(1,n):
    mgcd = math.gcd(mgcd, masses[i])

for i in range(n):
    print(int(masses[i] // mgcd), end = ' ')