"""
faça um programa que leia um conjunto não determinado de valores, e
para cada valor retorne:
- o quadrado
- o cubo
- a raiz quadrada
se for digitado um valor negativo ou zero finalizar o programa
"""

n = float(input("Insira um valor para receber:\n"
                "- o valor ao quadrado\n"
                "- o valor ao cubo\n"
                "- a raiza quadrada\n"
                "ou zero ou um número negativo para sair\n"
                "Valor: "))

while n > 0:
    n = float(input("Insira um valor para receber:\n"
                    "- o valor ao quadrado\n"
                    "- o valor ao cubo\n"
                    "- a raiza quadrada\n"
                    "ou zero ou um número negativo para sair\n"
                    "Valor: "))
    if n >= 0:
        print(f"{n} ao quadrado é igual a {n ** 2:.2f}\n"
              f"{n} ao cubo é igual a {n ** 3:.2f}\n"
              f"A raiz quadrada de {n} é igual a {n ** 0.5:.2f}\n")
    else:
        break

