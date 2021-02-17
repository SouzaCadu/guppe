"""
Compare 2 números e exiba o maior deles
"""

print("Comparando 2 valores:")
v1, v2 = float(input("Insira o primeiro valor:")), float(input("Insira o segundo valor:"))

if v1 > v2:
    print(f"{v1} é o maior valor")
else:
    print(f"{v2} é o maior valor")
