import sys

def binary_search(target, array):
  start = 0
  end = len(array) - 1

  while start <= end:
    mid = (start + end) // 2

    if target == array[mid]:
      print(1)
      return 1
    elif target < array[mid]:
      end = mid - 1
    else:
      start = mid + 1
  print(0)
  return 0

n = int(sys.stdin.readline())
arr_n = list(map(int, sys.stdin.readline().split()))
arr_n.sort()

m = int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))

for i in arr_m:
  binary_search(i, arr_n)