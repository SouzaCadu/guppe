"""
Determine se um ano é bissexto
"""

ano = int(input("Digite um ano, no formato AAAA, para saber se ele é bissetxo?"))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
