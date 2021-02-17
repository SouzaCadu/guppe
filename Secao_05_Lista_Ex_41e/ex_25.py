"""
Calcule as raízes da equação do segundo grau
"""

from math import sqrt

print("Informe 3 valores para saber as raízes da equação de segundo grau. \n"
      "Equação ax2 + bx + c, valores:")

a = float(input("Digite o valore de a:"))
b = float(input("Digite o valore de b:"))
c = float(input("Digite o valore de c:"))

d = b ** 2 - 4 * a * c

if d < 0:
    print(f"Delta menor que zero. Não existe raiz.")
elif d == 0:
    x1 = (-b + sqrt(d)) / 2 * a
    print(f"Raiz única {x1:.2f}.")
elif d > 0:
    x1 = (-b + sqrt(d)) / 2 * a
    x2 = (-b - sqrt(d)) / 2 * a
    print(f"As raízes são {x1:.2f} e {x2:.2f}.")
