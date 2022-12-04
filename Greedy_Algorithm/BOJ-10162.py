sec = [300, 60, 10]
t = int(input())
res = [0, 0, 0]
result = ''

for idx, i in enumerate(sec):
  res[idx] += t // i
  t %= i

result = ' '.join(str(s) for s in res)

if t % 10 != 0:
  print(-1)
else:
  print(result)