"""
51) Escreva um programa que leia as coordenadas x e y de pontos
no R² e calcule sua distância da origem (0, 0)
"""

import math

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

resultado = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

print("\nSua distância é %.2f" % resultado)