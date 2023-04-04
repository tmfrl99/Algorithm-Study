import sys
from collections import deque

def bfs(x, y):
  queue = deque([(x, y)])
  map[x][y] = 0
  cnt = 1
  
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<n and map[nx][ny] == 1:
        map[nx][ny] = map[x][y] + 1
        queue.append((nx, ny))
        map[nx][ny] = 0
        cnt += 1
  if cnt != 0:
    ans.append(cnt)

n = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = []

for i in range(n):
  for j in range(n):
    if map[i][j] == 1:
      bfs(i, j)

print(len(ans))
ans.sort()
for i in ans:
  print(i)