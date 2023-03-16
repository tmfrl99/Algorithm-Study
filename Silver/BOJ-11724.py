import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(start, end):

  visited[start] = True
  
  for i in graph[start]:
    if not visited[i]:
      dfs(i, end+1)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [False] * (n+1)
count = 0

for i in range(1, n+1):
  if not visited[i]:
    if not graph[i]:
      count += 1
      visited[i] = True
    else:
      dfs(i, 0)
      count += 1

print(count)