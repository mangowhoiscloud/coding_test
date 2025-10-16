import sys

input = sys.stdin.readline

n = int(input())
parents  = list(map(int, input().split()))
dnode = int(input())
isLeaf  = [True  for _ in range(n)]
deleted = [False for _ in range(n)]
visited = [False for _ in range(n)]
children = [0 for _ in range(n)]

cque = list()
answer = 0

for node in range(0, n):
    parent = parents[node]
    if parent != -1:
        isLeaf[parent] = False
        children[parent] += 1

def delNode():
    cque = list()
    cque.append(dnode)

    while len(cque) > 0:
        here   = cque.pop(0)
        parent = parents[here]
        deleted[here] = True
        if parent != -1:
            children[parent] -= 1
        for node in range(0, n):
            if here == parents[node]:
                cque.append(node)

delNode()

for node in range(0, n):
    if children[node] == 0 and not deleted[node]:
        answer += 1

delNode()

print(answer)