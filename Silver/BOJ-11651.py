import sys

n = int(sys.stdin.readline())
dot = []
for i in range(n):
  dot.append(list(map(int, sys.stdin.readline().split())))

dot.sort(key = lambda x:(x[1], x[0]))

for i, j in dot:
  print(i, j)