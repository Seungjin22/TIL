def fibo_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
       
def fibo_for(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return b