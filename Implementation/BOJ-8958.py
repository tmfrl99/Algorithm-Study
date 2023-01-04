n = int(input())
score = []

for i in range(n):
  score.append(input())

for i in range(n):
  answer = 0
  stack = 1
  for x in score[i]:
    if x == 'O':
      answer += stack
      stack += 1
    elif x == 'X':
      stack = 1
  print(answer)