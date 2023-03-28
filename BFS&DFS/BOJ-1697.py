import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(n):
  queue = deque()
  queue.append(n)

  while queue:
    n = queue.popleft()
    if n == k:
      print(visited[n])
      break
    else:
      for i in [n-1, n+1, n*2]:
        if 0 <= i <= 100000 and not visited[i]:
          visited[i] = visited[n] + 1
          queue.append(i)
          
n, k = map(int, input().split())
visited = [0] * 100001

bfs(n)