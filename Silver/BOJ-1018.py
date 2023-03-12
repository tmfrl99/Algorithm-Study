import sys
n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n)]
count = []

for a in range(n-7):
  for b in range(m-7):
    count_w = 0
    count_b = 0
    for i in range(a, a+8):
      for j in range(b, b+8):
        if (i+j) % 2 == 0:
          if board[i][j] != 'W':
            count_w += 1
          elif board[i][j] != 'B':
            count_b += 1
        else:
          if board[i][j] != 'B':
            count_w += 1
          elif board[i][j] != 'W':
            count_b += 1

    count.append(min(count_w, count_b))

print(min(count))