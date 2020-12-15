"""
Faça um programa que calcule a área do triângulo, cuja base
e altura são fornecidas pelo usuário.
Não devem ser aceitas medidas menores que zero.
"""

print("Informe os parametros para cálculo da área do triangulo.")

base = float(input("Valor da base: "))
h = float(input("Valor da altura: "))

while base <= 0 or h <= 0:
    print("Informe valores maiores que 0.")
    base = float(input("Valor da base: "))
    h = float(input("Valor da altura: "))

print(f"A área do triângulo é {(base * h) / 2:.2f}.")
