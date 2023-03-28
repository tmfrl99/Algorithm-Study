import sys
n, m = map(int, sys.stdin.readline().split())
res = []

def solve(start):
  if len(res) == m:
    print(" ".join(map(str, res)))
    return
    
  for i in range(start, n+1):
    res.append(i)
    solve(i)
    res.pop()
    
solve(1)