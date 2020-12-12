"""
Calculadora
- desconto de 10% a vista
- parcela em 3x sem juros
- comissão 5% sobre o valor a vista
- comissão 5% sobre o valor parcelado
"""

print(f"Insira o valor da venda:")

v = float(input())

print(f"Com desconto 10% à vista {v * 0.9:.2f} \n"
      f"Parcela 3x sem juros {v / 3:.2f} \n"
      f"Comissão sobre o valor à vista {(v * 0.9) * 0.05:.2f} \n"
      f"Comissão sobre o valor parcelado {v * 0.05:.2f}")