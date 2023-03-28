import sys

n = int(sys.stdin.readline())

words = []
for i in range(n):
  words.append(str(sys.stdin.readline().strip()))

set_words = list(set(words))

len_words = []
for i in set_words:
  len_words.append((len(i), i))

sorted_words = sorted(len_words)

for length, word in sorted_words:
  print(word)