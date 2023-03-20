t = int(input())
for i in range(t):
  r, s = input().split()
  p = ''
  for j in range(len(s)):
    p += s[j] * int(r)
  print(p)