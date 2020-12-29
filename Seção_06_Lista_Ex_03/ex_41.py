"""
faça um programa para calcular a associação em paralelo de 2 resistores
R1  e R2 fornecidos pelo usuário.
O programa deve ser executado até o valor digitado de uma das
resistências seja 0
"""

print("Digite os valores das resistências ou zero para sair.")

r1 = float(input("Digite o valor da resistência 1: "))
r2 = float(input("Digite o valor da resistência 2: "))

if r2 == 0:
    print("O valor dever ser diferente de 0.")
    r2 = float(input("Digite o valor da resistência 2: "))

print(f"O valor da associação em paralelo das resistências é {(r1 * r2) / (r1 + r2):.2f}.")

while r1 != 0 and r2 != 0:
    r1 = float(input("Digite o valor da resistência 1: "))
    r2 = float(input("Digite o valor da resistência 2: "))
    if r1 == 0 or r2 == 0:
        break
    else:
        print(f"O valor da associação em paralelo das resistências é {(r1 * r2) / (r1 + r2):.2f}.")

