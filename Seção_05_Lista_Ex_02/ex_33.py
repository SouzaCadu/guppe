"""
Calculadora de aumento de preço
"""

print("Tabela de reajustes: \n"
      "Preço antigo         | Reajuste \n"
      "até R$ 50            |    5% \n"
      "entre R$ 50 e R$ 100 |   10% \n"
      "acima de R$ 100      |   15%")

print()
p = float(input("Digite o preço antigo:"))

print()
if p < 50:
    p1 = p * 1.05
    if p1 <= 80:
        print(f"O preço novo é {p1:.2f}. Barato!")
elif 50 <= p <= 100:
    p1 = p * 1.10
    if p1 <= 80:
        print(f"O preço novo é {p1:.2f}. Barato!")
    elif 80 < p1 <= 120:
        print(f"O preço novo é {p1:.2f}. Normal!")
elif p > 100:
    p1 = p * 1.15
    if 120 < p1 <= 200:
        print(f"O preço novo é {p1:.2f}. Caro!")
    elif p1 > 200:
        print(f"O preço novo é {p1:.2f}. Muito caro!")
