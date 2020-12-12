"""
Se o número digitado for positivo:
- calcule o quadrado
- calcule a raiz quadrada
"""

v1 = float(input("Digite um valor positivo para saber o quadrado e a raiz quadrada:"))

if v1 > 0:
    print(f"O quadrado de {v1} é {v1 ** 2:.2f} e a raiz quadrada é {v1 ** 0.5:.2f}")
else:
    print("Digite um valor positivo.")