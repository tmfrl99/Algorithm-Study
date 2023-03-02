from collections import deque
import sys

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
for i in range(m):
  x, y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1, n+1):
  graph[i].sort()
  
visited = [False] * (n+1)
dfs(graph, v, visited)
print()

visited = [False] * (n+1)
bfs(graph, v, visited)