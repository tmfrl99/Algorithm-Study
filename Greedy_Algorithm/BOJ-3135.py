a, b = map(int, input().split())
n = int(input())
mhz = []
for i in range(n):
  mhz.append(int(input()))

num1 = abs(b-a)

for i in range(n):
  mhz[i] = abs(b-mhz[i])
num2 = min(mhz)

print(min(num1, num2+1))