"""
Faça um programa que receba 2 números: Calcule e mostre:
- a soma dos números pares desse intervalo de números,
incluindo os números digitados
- a multiplicação dos números ímpares desse intervalo,
incluindo os digitados
"""

print("Digite 2 números e receba:\n"
      "A soma dos números pares desse intervalo, incluindo os números digitados.\n"
      "A multiplicação dos números ímpares desse intervalo, incluindo os números digitados.")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

while n1 > n2 or n1 == n2:
    print('O valor do segundo número deve ser maior que o valor do primeiro')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

pares = []
impares = []
soma = 0
multi = 1

for n in range(n1, n2+1):
    if n % 2 == 0:
        pares.append(n)
        for par in pares:
            soma = soma + par
    else:
        impares.append(n)
        for impar in impares:
            multi = multi * impar

print(f"A soma dos pares é igual a {soma}\n"
      f"e a multiplicação dos ímpares é igual a {multi}.")
