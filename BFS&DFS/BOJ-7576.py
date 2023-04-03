import sys
from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

m, n = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))

bfs()

res = max(map(max, box)) - 1
for tomato in box:
    if 0 in tomato:
        res = -1

print(res)