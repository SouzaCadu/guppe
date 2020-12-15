"""
Faça um programa que leia vários números inteiros positivos
se um número negativo for digitado o programa deve ser encerrado
e exibir o maior e o menor valor
"""
i = 1

menor = maior = 0

print("Digite quantos números inteiros positivos desejar\n"
      "ao digitar um inteiro negativo serão exibidos\n"
      "o maior e o menor valor digitados.")

n = int(input("Digite um número: "))

while n >= 0:
    n = int(input("Digite um número: "))
    if n <= menor:
        menor = n
    if n >= maior:
        maior = n
else:
    print(f"O maior número é {maior} e o menor número é {menor}.")