"""
Peça 10 valores como input e exiba a soma
"""

print("A seguir digite 10 números para saber a soma deles")
i = 1
soma = 0
while i <= 10:
    n = float(input("Digite um valor:"))
    i = i + 1
    soma = soma + n
print(f"A soma dos valores digitados é {soma}")