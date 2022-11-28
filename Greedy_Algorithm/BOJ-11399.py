n = int(input())
time = list(map(int, input().split()))
lst = []
result = 0
time.sort()

for i in time:
  result += i
  lst.append(result)

print(sum(lst))