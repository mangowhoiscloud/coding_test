import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
tree = [[] for _ in range(n+1)]
treeRev = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
time = [0 for _ in range(n+1)]

que = list()
ans = [0,0] # time, count

for i in range(m):
    here, there, cost = list(map(int, input().split()))
    tree[here].append((there, cost))
    treeRev[there].append((here, cost))
    indegree[there] += 1

startCity, endCity = list(map(int, input().split()))

que.append(startCity)

while len(que) > 0:
    here = que.pop(0)
    for there, cost in tree[here]:
        indegree[there] -= 1
        time[there] = max(time[there], time[here] + cost)
        if indegree[there] == 0:
            que.append(there)
ans[0] = time[endCity]

que.clear()
que.append(endCity)
visited[endCity] = True

while len(que) > 0:
    here = que.pop(0)
    for there, cost in treeRev[here]:
        if time[there] + cost == time[here]:
            ans[1] += 1
            if not visited[there]:
                visited[there] = True
                que.append(there)

print(ans[0])
print(ans[1])