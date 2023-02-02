n = int(input())
ps = []

for i in range(n):
  ps.append(input())

for i in range(len(ps)):
  sum = 0
  for j in ps[i]:
    if j == "(":
      sum += 1
    elif j == ")":
      sum -= 1
    if sum < 0:
      print("NO")
      break
  if sum > 0:
    print("NO")
  elif sum == 0:
    print("YES")
    