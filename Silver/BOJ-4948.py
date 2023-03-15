import sys

N = 123456 * 2 + 1

check = [False, False] + [True] * (N-1)
for i in range(2, int(N**0.5)+1):
      if check[i]:
        for j in range(2*i, N+1, i):
          check[j] = False
          
while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break

  count = 0
  for i in range(n+1, 2*n+1):
    if check[i]:
      count += 1
  
  print(count)