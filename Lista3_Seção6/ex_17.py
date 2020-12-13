"""
faça um programa que leia um inteiro positivo N e calcule
a soma dos N primeiros números naturais
"""

print("Digite um inteiro positivos para saber a soma dos\n"
      "N primeiros números naturais.")
soma = 0
n = int(input("Digite um inteiro positivo: "))

for i in range(n+1):
    soma = soma + i
print(f"A soma dos {n} números naturais é {soma}.")
