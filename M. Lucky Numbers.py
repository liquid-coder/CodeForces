inp1, inp2 = map(int, input().split())
count = 0

for i in range(inp1, inp2 + 1):

  for j in str(i):
    if j not in ['4', '7']:
      break
  else:
        print(i, end=" ")
        count += 1

if count == 0:
    print('-1')
