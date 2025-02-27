import math

test_cases = int(input())
for i in range(test_cases):
    l, r = map(int, input().split())
    if l == r:
        
        if math.gcd(l, r) == 1:
            print(1)
        else:
            print(0)
    else:
        print(r - l)