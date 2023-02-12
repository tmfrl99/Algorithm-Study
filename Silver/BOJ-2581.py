m = int(input())
n = int(input())

check = [True for i in range(n+1)]
for i in range(2, int(n**0.6)):
  if check[i] == True:
    for j in range(2*i, n+1, i):
      check[j] = False

prime = []
for i in range(m, n+1):
  if i >= 2:
    if check[i] == True:
      prime.append(i)
      
if len(prime) == 0:
  print(-1)
else:
  print(sum(prime))
  print(min(prime))