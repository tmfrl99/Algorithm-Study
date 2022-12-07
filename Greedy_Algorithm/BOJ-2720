t = int(input())
c = []
money = [25, 10, 5, 1]

for i in range(t):
  c.append(int(input()))

for i in c: 
  change = [0, 0, 0, 0]
  for idx, j in enumerate(money): 
    change[idx] = i // j 
    i %= j
  print(" ".join(map(str, change)))