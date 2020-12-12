"""
A partir da altura e do sexo calcule o peso ideal
"""

g, h = str(input("Informe o genêro (M/F):")).lower(), float(input("Informe a altura em metros:"))

if g == "m":
    print(f"O peso ideal é {(72.7 * h) - 58:.2f}.")
else:
    print(f"O peso ideal é {(62.1 * h) - 44.7:.2f}.")
