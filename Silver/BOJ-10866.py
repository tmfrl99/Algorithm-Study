from collections import deque
import sys

dq = deque()
n = int(sys.stdin.readline())

for i in range(n):
  order = sys.stdin.readline().split()
  
  if order[0] == 'push_front':
    dq.appendleft(order[1])
  if order[0] == 'push_back':
    dq.append(order[1])
  if order[0] == 'pop_front':
    if not dq:
      print(-1)
    else:
      tmp = dq.popleft()
      print(tmp)
  if order[0] == 'pop_back':
    if not dq:
      print(-1)
    else:
      tmp = dq.pop()
      print(tmp)
  if order[0] == 'size':
    print(len(dq))
  if order[0] == 'empty':
    if not dq:
      print(1)
    else:
      print(0)
  if order[0] == 'front':
    if not dq:
      print(-1)
    else:
      print(dq[0])
  if order[0] == 'back':
    if not dq:
      print(-1)
    else:
      print(dq[len(dq)-1])