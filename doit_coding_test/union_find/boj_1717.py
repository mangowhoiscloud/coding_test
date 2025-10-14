import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = list(map(int, input().split()))
parent = [i for i in range(0, n+1)]

def union(a, b):
    rootA, rootB = find(a), find(b)
    if rootA > rootB:
        rootA, rootB = rootB, rootA
    if rootA != rootB:
        parent[rootB] = rootA

def find(node):
    if node == parent[node]:
        return node
    else:
        parent[node] = find(parent[node])
        return parent[node]

def checkSame(a, b):
    return find(a) == find(b)

for _ in range(m):
    command = list(map(int, input().split()))
    if command[0] == 0:
        union(command[1], command[2])
    elif checkSame(command[1], command[2]):
        print("YES")
    else:
        print("NO")