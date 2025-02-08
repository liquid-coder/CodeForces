inp = input()
inverse = inp[::-1]
cut = inverse.strip('0')
print(cut)
if inverse == inp:
    print('YES')
else:
    print('NO')
    
