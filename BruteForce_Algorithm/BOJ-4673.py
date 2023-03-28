def d(n):
  for i in str(n):
    n += int(i)
  return n
    
self_num = list(range(1,10001))

for i in range(1, 10001):
  if d(i) in self_num:
    self_num.remove(d(i))

for i in range(len(self_num)):
  print(self_num[i])