import sys

def decom(n):
  num = 0
  for i in str(n):
    num += int(i)
  return num

n = int(sys.stdin.readline())
res = 0

for i in range(1, n):
  if i + decom(i) == n:
    res = i
    break

print(res)