"""
Dividir um valor por 46%, 32% e o restante
"""

print(f"O valor inicial é de:")

v = float(input())
p1 = 0.46
p2 = 0.34
p3 = 1 - p1 - p2

print(f"46% do valor é {p1 * v:.2f}, \n"
      f"32% do valor é {p2 * v:.2f}, \n"
        f"o restante é {p3 * v:.2f}")