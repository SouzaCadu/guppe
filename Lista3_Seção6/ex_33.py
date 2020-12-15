"""
Dados n e dois números inteiros positivos, i e j, diferente de 0,
imprimir primeiros naturais que são múltiplos de i ou j ou de ambos
"""

print("Digite a quantidade números múltiplos desejados\n"
      "para 2 números a sua escolha.")
print()
n = int(input("Digite a quantidade de múltiplos desejados: "))
i = int(input("Primeira variável: "))
j = int(input("Segunda variável: "))

aux = 0
contador = 0

while True:
    if aux % i == 0 or aux % j == 0:
        print(aux, end=" ")
        contador += 1
    aux += 1
    if contador == n:
        break
