import sys
input = sys.stdin.readline

c = int(input())
for i in range(c):
  n = list(map(int, input().split()))
  avg = sum(n[1:])/n[0]
  lst = list(j for j in n[1:] if j>avg)
  res = round((len(lst)/n[0]*100), 3)
  print(f'{res:.3f}%')