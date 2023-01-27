a = int(input())
b = list(input())
b.reverse()
num = []
for i in range(len(b)): 
  num.append(a*int(b[i])*(10**i))
  print(a*int(b[i]))
print(sum(num))