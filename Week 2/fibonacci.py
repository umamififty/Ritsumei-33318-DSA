# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(10))

def fibo_linear(n):
    if n <= 1:
        return n, 0
    else:
        a, b = fibo_linear(n-1)
        return a + b, a
    
print(fibo_linear(10))