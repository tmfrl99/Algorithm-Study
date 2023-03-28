n = input().replace('9', '6')
set = [0] * 9

for i in n:
  set[int(i)] = n.count(i)
set[6] = set[6] // 2 + set[6] % 2

print(max(set))