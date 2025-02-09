A, B = map(int, input().split())
inp1 = input()

if len(inp1) != A + B + 1:
    print('No')
else:
    check = True
    if inp1[A] != '-':
        check = False
    else:
        for i in range(A + B + 1):
            if i != A:
                if not ('0' <= inp1[i] <= '9'):
                    check = False
                    break

    if check:
        print('Yes')
    else:
        print('No')
