n, k = map(int,input().split())
coin = []
result = 0

for i in range(n):
  coin.append(int(input()))
coin.sort(reverse=True)

for i in coin:
  result += k // i
  k %= i

print(result)
  