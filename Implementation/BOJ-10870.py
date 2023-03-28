def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    num[n] = fibo(n-1) + fibo(n-2)
    return num[n]

n = int(input())
num = [0] * 21

print(fibo(n))