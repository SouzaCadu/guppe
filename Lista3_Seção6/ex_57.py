"""
faça um programa que conte quantos números primos existem
em um intervalo dado por A e B, informados pelo usuário
"""
print("Digite um intervalo para saber quantos números primos existem nele.")

int1 = int(input("Digite o primeiro número inteiro: "))
if int1 == 1:
    print("Valor inválido.")
    int1 = int(input("Digite o primeiro número inteiro: "))

int2 = int(input("Digite o segundo número inteiro: "))
if int2 <= int1:
    print("Valor inválido.")
    int2 = int(input("Digite o segundo número inteiro: "))

lista = []

for i in range(int1, int2 + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lista.append(i)

print(f"A sequencia entre {int1} e {int2} é {lista}", end=" ")