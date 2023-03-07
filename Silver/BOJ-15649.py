import sys
n, m = map(int, sys.stdin.readline().split())
res = []
visited = [False] * n

def solve(d, n, m):
  if d == m:
    print(" ".join(map(str, res)))
    return
    
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      res.append(i+1)
      solve(d+1, n, m)
      visited[i] = False
      res.pop()

solve(0, n, m)