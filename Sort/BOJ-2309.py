h = [int(input()) for _ in range(9)]

temp = sum(h) - 100

for i in range(8):
  for j in range(i+1, 9):
    if h[i] + h[j] == temp:
      a = h[i]
      b = h[j]

h.remove(a)
h.remove(b)
h.sort()

for i in h:
  print(i)