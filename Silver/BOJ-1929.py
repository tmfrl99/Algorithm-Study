m, n = map(int,input().split())

check = [True]*(n+1)

for i in range(2, int(n**0.5)+1):
  if check[i] == True:
    for j in range(2*i, n+1, i):
      check[j] = False

for i in range(m, n+1):
  if check[i] and i > 1:
    print(i)