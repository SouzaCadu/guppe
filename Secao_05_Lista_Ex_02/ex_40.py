"""
Custo de um carro é a soma
- Custo de fábrica
- % distribuidor
- % comissão do vendedor
"""

print("Cálculo do custo final de um veículo: \n"
      "Preço de fábrica            | % distribuidor | % Impostos  \n"
      "Até R$ 12.000               |    5%          |  isento     \n"
      "Entre R$ 12.000 e R$ 25.000 |   10%          |  15%        \n"
      "Acima de R$ 25.000          |   15%          |  20%        \n")

custo = float(input("Informe o preço de fábrica:"))

if custo < 12000:
    print(f"Custo total é de R$ {custo * 1.05:.2f}.")
elif 12000 <= custo <= 25000:
    print(f"Custo total é de R$ {(custo * 1.10) * 1.15:.2f}.")
elif custo > 25000:
    print(f"Custo total é de R$v{(custo * 1.15) * 1.2:.2f}.")
else:
    print("Valor inválido.")
