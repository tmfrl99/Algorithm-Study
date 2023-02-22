import sys
k = int(sys.stdin.readline())
num = []
for i in range(k):
  n = int(sys.stdin.readline())
  if n != 0:
    num.append(n)
  else:
    num.pop()

print(sum(num))