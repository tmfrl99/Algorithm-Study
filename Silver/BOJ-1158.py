from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])

res = []
i = 1
while queue:
  if i % k == 0:
    res.append(queue.popleft())
  else:
    queue.append(queue.popleft())
  i += 1

print('<' + ', '.join(map(str, res)) + '>')