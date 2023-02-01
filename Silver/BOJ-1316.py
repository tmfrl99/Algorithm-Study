n = int(input())

for i in range(n):
  word = list(input())
  alpha = []
  for idx, j in enumerate(word):
    if j in alpha and word[idx] != word[idx-1]:
      n -= 1
      break
    else:
      alpha.append(j)
print(n)