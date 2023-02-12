import sys

n = int(sys.stdin.readline())
dot = []
for i in range(n):
  dot.append(list(map(int, sys.stdin.readline().split())))

dot.sort()

for i, j in dot:
  print(i, j)