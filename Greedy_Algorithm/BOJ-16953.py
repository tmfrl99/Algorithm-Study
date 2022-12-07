a, b = map(int, input().split())
cnt = 0

while True:
  if b % 2 == 0:
    b /= 2
  else:
    b -= 1
    b /= 10
  cnt += 1
  if b <= a:
    break

if b < a:
  print(-1)
else:
  print(cnt + 1)