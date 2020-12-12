"""
verifique se um número é divisivel por 3 ou 5,
mas não simultaneamente pelos dois
"""

n = float(input("Digite um número para saber se é divisível por 3 ou por 5:"))

if n % 3 == 0 or n % 5 == 0:
    print(f"{n} é divisível por 3 ou por 5.")
else:
    print("Condição não atendida.")
