inp1 = input()
output = []
check_str = ''
balance = 0
for i in inp1:
    check_str+=i
    if i == 'L':
        balance += 1
    else:
        balance -= 1
    if balance == 0:
        output.append(check_str)
        check_str = ''
        
print(len(output))
for i in output:
    print(i)