n = int(input())
white_paper = [[0]*100 for _ in range(100)]
area = 0

for i in range(n):
  x, y = map(int, input().split())

  for i in range(x, x+10):
    for j in range(y, y+10):
      white_paper[i][j] = 1

for i in white_paper:
  if 1 in i:
    area += sum(i)

print(area)
    