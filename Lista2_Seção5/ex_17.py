"""
calcule a área de um trapézio
"""

from sys import exit

print("Calculadora da área do trapézio:")
print()
bma = float(input("Digite o valor da base maior:"))
if bma <= 0:
    exit("Valor deve ser maior que zero.")

bme = float(input("Digite o valor da base menor:"))
if bme <= 0:
    exit("Valor deve ser maior que zero.")

h = float(input("Digite o valor da altura:"))
if h <= 0:
    exit("Valor deve ser maior que zero.")

print(f"A área do trapézio é {((bma + bme) * h) / 2:.2f}")
