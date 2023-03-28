import sys

def dfs(graph, v, visited):
  global cnt
  visited[v] = True

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
      cnt += 1
        
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
for i in range(m):
  x, y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [False] * (n+1)
cnt = 0

dfs(graph, 1, visited)
print(cnt)