"""
De acordo com peso e altura de uma pessoa faça uma classificação
"""

peso = float(input("Insira o peso de uma pessoa:"))

altura = float(input("Insira a altura de uma pessoa:"))

if altura < 1.20:
    if peso < 60:
        print("A")
    elif 60 <= peso <= 90:
        print("D")
    else:
        print("G")
elif 1.20 <= altura <= 1.70:
    if peso < 60:
        print("B")
    elif 60 <= peso <= 90:
        print("E")
    else:
        print("H")
else:
    if peso < 60:
        print("C")
    elif 60 <= peso <= 90:
        print("F")
    else:
        print("I")
