import sys

n = int(sys.stdin.readline())
mem = []
for i in range(n):
  mem.append(list(sys.stdin.readline().split()))

mem.sort(key = lambda x:int(x[0]))

for i, j in mem:
  print(i, j)