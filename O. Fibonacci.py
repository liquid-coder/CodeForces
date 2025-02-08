inp1 = int(input())  
def fibonacci(inp1):
    if inp1 == 1:
        return 0
    elif inp1 == 2:
        return 1
    else:
        return fibonacci(inp1 - 1) + fibonacci(inp1 - 2)

output = fibonacci(inp1)
print(output)  