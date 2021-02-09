"""
faça um programa que preencha um vetor de tamanho 100 com os 100
primeiros números naturais que não são múltiplos de 7 ou
que terminam com 7
"""

i = 1
lista = []

while True:
    if i % 7 != 0 and list(str(i))[- 1] != "7":
        lista.append(i)
        i += 1
    else:
        i += 1
    if len(lista) > 100:
        break
print(lista)