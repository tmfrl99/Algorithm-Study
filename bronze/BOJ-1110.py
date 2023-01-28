n = int(input())
k = n 
ans = 0

while True: 
  if k < 10:
    k = int('0' + str(k))
  k = (k%10)*10 + (((k//10)+(k%10))%10)
  ans += 1
  if k == n:
    break
print(ans)