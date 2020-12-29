"""
Faça um programa que some os números ímpares contidos em um intervalo definido pelo usuário
O usuário define o valor inicial do intervalo e valor final
"""

print("Defina um valor inicial e um valor final para saber\n"
      "a soma de todos os valores ímpares contidos nesse intervalo.")

ini = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

while ini > fim:
    print("O valor inicial deve ser menor que o valor final.")
    ini = int(input("Digite o valor inicial: "))
    fim = int(input("Digite o valor final: "))

soma = 0

for i in range(ini, fim + 1):
    if i % 2 != 0:
        soma += i
print(f"A soma dos ímpares no intervalo entre {ini} e {fim} é {soma}.")