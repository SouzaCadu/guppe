"""
Leia um número positivo do usuário, então, calcule e imprima a sequencia Fibonacci até
o primeiro número superior ao número lido.
Exemplo: se o usuário informou o número 30, a sequencia a ser
impressa será 0 1 1 2 3 5 8 13 21 34
"""

n = int(input('Insira um número positivo para gerar a sequência de Fibonnaci: '))

a = c = 0
b = 1

lista = [0, 1]

while c <= n:
    c = a + b
    lista.append(c)
    a = b
    b = c
print(lista)