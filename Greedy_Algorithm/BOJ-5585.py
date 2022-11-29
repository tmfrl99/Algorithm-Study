n = int(input())
money = [500, 100, 50, 10, 5, 1]

pay = 1000 - n
result = 0

for i in money:
  result += pay // i
  pay %= i

print(result)