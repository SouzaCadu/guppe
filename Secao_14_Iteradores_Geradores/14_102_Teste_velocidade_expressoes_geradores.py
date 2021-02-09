"""
Teste de velocidade com expressões gerdoras

# formas de diferenciar Generator x Generator Function

# Generator


def nums():
    for num in range(10):
        yield num


ge1 = nums()
print(ge1)
print(next(ge1))
print(next(ge1))


# Generator expression


ge2 = (num for num in range(10))

print(ge2)
print(next(ge2))
print(next(ge2))

import time


# Realizando o teste de velocidade
# Generator expression
gen_inicio = time.time()
print(sum(num for num in range(10**7)))
gen_tempo = time.time() - gen_inicio

# List comprehension
list_inicio = time.time()
print(sum([num for num in range(10**7)]))
list_tempo = time.time() - list_inicio

print(f"Generator expression levou {gen_tempo:.2f} tempo.")
print(f"List comprehension levou {list_tempo:.2f} tempo.")


"""

