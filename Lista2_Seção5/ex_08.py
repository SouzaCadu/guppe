"""
verifique se os valores digitados estão entre 0.0 e 10.0
e calcule a média
"""

import sys

print("Informe as duas notas do aluno para saber a média.")

v1 = float(input("Digite a primeira nota:"))

if 0.0 <= v1 <= 10.0:
    pass
else:
    sys.exit(print("Nota inválida. Programa finalizado."))

v2 = float(input("Digite a segunda nota:"))

if 0.0 <= v2 <= 10.0:
    print(f"A média das notas é {(v1 + v2) / 2:.2f}.")
else:
    sys.exit(print("Nota inválida. Programa finalizado."))
