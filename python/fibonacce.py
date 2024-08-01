def fibonacci_recursive(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

def fibonacci_interactive(n):
    a,b = 0,1

    for i in range(n):
        a,b=b,a+b
    return a

n = 10
print(f"fibonacci sequence upto{n} (recursive):")
for i in range(n):
    print(fibonacci_recursive(i),end=" ")

n = int(input("Enter your valu:"))
print(f"fibonacci sequence upto{n} (interactive)")
for i in range(n):
    print(fibonacci_interactive(i),end=" ")