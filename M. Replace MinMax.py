inp1 = int(input())  
arr = list(map(int, input().split()))  
min_value = arr[0]
max_value = arr[0]
min_index = 0
max_index = 0
for i in range(1, inp1):
    if arr[i] < min_value:
        min_value = arr[i]
        min_index = i
    if arr[i] > max_value:
        max_value = arr[i]
        max_index = i
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
for num in arr:
    print(num, end=' ')