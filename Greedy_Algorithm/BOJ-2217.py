n = int(input())
w = []
for i in range(n):
  w.append(int(input()))
res = []

w.sort(reverse=True)
for i in range(len(w)):
  res.append(w[i]*(i+1))

print(max(res))