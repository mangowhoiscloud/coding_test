import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
maze = [[0] * (M+1) for _ in range(N+1)]
visited = [[0] * (M+1) for _ in range(N+1)]
dy   = [1, 0, -1, 0]
dx   = [0, 1, 0, -1]

# (y, x)

for i in range(1, N+1):
    row = list(input())
    for j in range(1, M+1):
        maze[i][j] = int(row[j-1])

def rangeCheck(y, x):
    return (1 <= y and y <= N) and (1 <= x and x <= M)

def BFS():
    ans = 0
    que = list()
    que.append((1,1))
    visited[1][1] = 1
    while len(que) > 0:
        hereY, hereX = que.pop(0)
        for i in range(4):
            thereY = hereY + dy[i]
            thereX = hereX + dx[i]
            if not rangeCheck(thereY, thereX)  : continue
            if not maze[thereY][thereX]    == 1: continue
            if not visited[thereY][thereX] == 0: continue
            visited[thereY][thereX] = visited[hereY][hereX] + 1
            que.append((thereY, thereX))

BFS()
print(visited[N][M])