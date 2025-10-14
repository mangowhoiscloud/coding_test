import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

def union(a, b):
    rootA, rootB = find(a), find(b)
    if rootA > rootB:
        rootA, rootB = rootB, rootA
    if rootA != rootB:
        parent[rootA] = rootB
    
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
    return parent[a]

def check(a,b):
    return find(a) == find(b)

for i in range(1, N+1):
    bridge = [-1] + list(map(int, input().split()))
    for j in range(1, N+1):
        if bridge[j] == 1:
            union(i, j)

plan = list(map(int, input().split()))
spanning = find(plan[0])

for i in range(0, len(plan)-1):
    if not check(plan[i], plan[i+1]):
        print("NO")
        exit(0)

print("YES")