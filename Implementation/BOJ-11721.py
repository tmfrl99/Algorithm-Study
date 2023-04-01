import sys

word = str(sys.stdin.readline())

for i in range(len(word)//10+1):
  print(word[i*10:(i+1)*10])