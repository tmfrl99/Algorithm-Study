n = int(input())
m = 2
res = []

while m <= n:
  if n % m == 0:
    n /= m
    res.append(m)
  else:
    m += 1

for i in res:
  print(i)