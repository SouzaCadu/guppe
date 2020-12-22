"""
leia 10 números inteiros e armazene em um vetor.
depois escreva os elementos que são primos e suas
respectivas posições no vetor
"""

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print("Insira 10 números reais para saber quais são primos.")

v1 = []
count = 1

while len(v1) < 10:
    valor1 = int(input(f"Digite {count} de 10 números: "))
    v1.append(valor1)
    count += 1
print(v1)

for i, j in enumerate(v1):
    if eh_primo(j):
        print(f'O valor {j} é primo e está na posição {i} do vetor')