s = int(input())
n = 0
res = 0

while True:
  n += 1
  res += n

  if res > s:
    break

print(n-1)