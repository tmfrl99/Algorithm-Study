from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
  order = sys.stdin.readline().strip()
  if 'push' in order:
    queue.append(order[5:])
  if 'pop' in order:
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
      queue.popleft()
  if 'size' in order:
    print(len(queue))
  if 'empty' in order:
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  if 'front' in order:
    if len(queue) == 0:
      print(-1)
    else: 
      print(queue[0])
  if 'back' in order:
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[len(queue)-1])