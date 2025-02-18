arr_length = int(input())
arr = list(map(int,input().split()))
c = 0
i=0
j = arr_length-1
while i < j:
    if arr[i] == arr[j]:
        c += 1
        i += 1
        j -= 1
    else:
        break
if c == arr_length//2:
    print('YES')
else:
    print('NO')
      

