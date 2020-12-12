"""
Verifique se os valores A, B e C podem ser os lados de um triangulo:
- o comprimento de cada lado é menor do que a soma dos outros dois lados
- equilátero se todos os lados forem iguais
- isósceles se 2 lados tem comprimentos iguais
- escaleno se 3 lados forem diferentes
"""

print("Insira três valores para saber se eles podem formar um triângulo.")

a = float(input("Insira o valor do primeiro lado:"))
b = float(input("Insira o valor do segundo lado:"))
c = float(input("Insira o valor do terceiro lado:"))

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    if a == b == c:
        print("Essas medidas formam um triângulo equilátero.")
    elif a == b or b == c or a == c:
        print("Essas medidas formam um triângulo isósceles.")
    else:
        print("Essas medidas formam um triângulo escaleno.")
else:
    print("Não é possível formar um triângulo com essas medidas.")
