res = []
for i in range(10):
  n = int(input())
  res.append(n%42)

set_res = set(res)
print(len(set_res))