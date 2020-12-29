"""
Dado 2 números inteiros:
 - qual o maior deles
 - a diferença entre eles
"""

print("Comparando 2 valores e calculando a diferença")
v1, v2 = int(input("Insira o primeiro valor:")), int(input("Insira o segundo valor:"))

if v1 > v2:
    print(f"{v1} é o maior valor e a diferença para {v2} é {v1-v2}.")
else:
    print(f"{v2} é o maior valor e a diferença para {v1} é {v2-v1}.")
