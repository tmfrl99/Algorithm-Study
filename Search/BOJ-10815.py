import sys

def binary_search(target, array): # 이진탐색
  start = 0
  end = n - 1
  
  while start <= end:
    mid = (start + end) // 2
    if target > array[mid]:
      start = mid + 1
    elif target < array[mid]:
      end = mid - 1
    else:
      print(1, end = ' ')
      break
  if start > end:
    print(0, end = ' ')

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
  binary_search(i, n_list)

# import sys

# n = int(sys.stdin.readline()) # 자료구조
# n_list = set(map(int, sys.stdin.readline().split()))

# m = int(sys.stdin.readline())
# m_list = list(map(int, sys.stdin.readline().split()))

# for i in m_list:
#   if i in n_list:
#     print(1, end = ' ')
#   else:
#     print(0, end = ' ')