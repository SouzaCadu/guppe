"""
faça um programa que leia um vetor de 10 números.
leia um número x, conte os múltiplos de x em um vetor e mostre-os em tela
"""

print("Insira 10 números e depois selecione 1 para saber se há algum múltiplo dele na lista.")

v1 = []
multiplos = []
count = 1

while count <= 10:
    valor = int(input(f"Digite {count} de 10 números: "))
    v1.append(valor)
    count += 1
    if count > 10:
        print(f"A lista de números digitados é {v1}.")
        multiplo = int(input("Selecione um valor da lista para saber se há algum múltiplo: "))
        for i in v1:
            if i % multiplo == 0:
                multiplos.append(i)
        print(f"A lista dos multiplos de {multiplo} é {multiplos}.")
