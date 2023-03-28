n = int(input())
num = list(map(int, input().split()))

count = 0
for i in num:
  check = 1
  for j in range(2, i):
    if i % j == 0:
      check = 0
      break
  if check and i != 1:
    count += 1

print(count)