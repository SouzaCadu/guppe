"""
Teste de memória com Generator

Usando listas:

def fibonacci(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


[print(i) for i in fibonacci(100000)]

474MB

def fibonacci_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1


[print(i) for i in fibonacci_gen(100000)]

4MB

"""

