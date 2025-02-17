s = input().split()
output = ''
for i in s:
    output+=i[::-1]+' '
print(output.strip())