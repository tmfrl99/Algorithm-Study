import sys
n, m = map(int, sys.stdin.readline().split())
res = []

def solve():
  if len(res) == m:
    print(" ".join(map(str, res)))
    return
    
  for i in range(1, n+1):
    res.append(i)
    solve()
    res.pop()
    
solve()