n = int(input())
parents = list(map(int, input().split()))
del_node = int(input())
tree = [[] for _ in range(n)]
visited = [False for _ in range(n)]
root = -1
ret  = 0

for child in range(n):
    parent = parents[child]
    if parent == -1:
        root = child
        continue
    tree[parent].append(child)

def dfs(here):
    global ret
    count = 0
    if here == del_node:
        return
    for child in tree[here]:
        if child == del_node: continue
        count += 1
        dfs(child)
    if count == 0:
        ret += 1
    
dfs(root)
print(ret)