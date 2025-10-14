import sys

input = sys.stdin.readline
n, m = list(map(int, input().split()))
stakeholders = list(map(int, input().split()))
parent = [i for i in range(n+1)]
party  = []
ans = 0

def union(a, b):
    global parent
    rootA, rootB = find(a), find(b)
    if rootA > rootB:
        rootA, rootB = rootB, rootA
    if rootA != rootB:
        parent[rootB] = rootA

def find(a):
    global parent
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def check(a,b):
    return find(a) == find(b)

def setStakeholders():
    global stakeholders
    del stakeholders[0]
    for person in stakeholders:
        union(0, person)

setStakeholders()

for _ in range(m):
    session = list(map(int, input().split()))
    del session[0]
    party.append(session)
    rep = session[0]
    for i in range(1, len(session)):
        union(rep, session[i])

for session in party:
    isPossible = True
    for person in session:
        if find(person) == 0:
            isPossible = False
            break
    if isPossible:
        ans += 1

print(ans)
