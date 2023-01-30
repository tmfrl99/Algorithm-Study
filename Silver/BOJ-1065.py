n = int(input())
cnt = 99

if n < 100:
  print(n)
else:
  for i in range(100, n+1):
    if (i%10)-((i//10)%10) == ((i//10)%10)-(i//100):
      cnt += 1
  print(cnt)