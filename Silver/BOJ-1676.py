import sys
from math import factorial

n = int(sys.stdin.readline())
fact = factorial(n)
cnt = 0

while fact % 10 == 0:
  fact = fact // 10
  cnt += 1

print(cnt)