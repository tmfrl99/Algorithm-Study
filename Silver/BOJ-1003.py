import sys

def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  if d[n] != 0:
    return d[n]
  d[n] = fibo(n-1) + fibo(n-2)
  return d[n]

t = int(sys.stdin.readline())
d = [0] * 41

for i in range(t):
  n = int(sys.stdin.readline())
  if n == 0:
    print(1, 0)
  elif n == 1:
    print(0, 1)
  else:
    print(fibo(n-1), fibo(n))