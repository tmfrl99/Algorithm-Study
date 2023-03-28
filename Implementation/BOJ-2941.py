alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in alpha:
  if i in word:
    word = word.replace(i, "a")  
    
print(len(word))