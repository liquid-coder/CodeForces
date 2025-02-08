test_case = int(input())
for i in range(test_case):
  arr_length = int(input())
  arr = list(map(int, input().split()))
  min_sum = 2 * (10 ** 6) + 100 
  for j in range(arr_length):
    for k in range(j+1,arr_length):
      new_sum = arr[j]+arr[k] + k-j
      if new_sum<min_sum:
        min_sum = new_sum
  print(min_sum)