"""
Calcule o preço final de acordo com a UF
"""

from sys import exit

print("Selecione a UF para saber o preço final \n"
      "com o respectivo imposto:"
      "1 - Minas Gerais        -  7.0% \n"
      "2 - São Paulo           -  8.0% \n"
      "3 - Rio de Janeiro      - 15.0% \n"
      "4 - Mato Grosso do Sul  -  8.0%")

uf = int(input("Digite o código da UF:"))

if uf not in (1, 2, 3, 4):
    exit(print("Código inválido!"))

preco = float(input("Informe o valor do produto"))

if uf == 1:
    print(f"O valor final é {preço * 1.07:.2f}.")
elif uf == 2:
    print(f"O valor final é {preço * 1.08:.2f}.")
elif uf == 3:
    print(f"O valor final é {preço * 1.15:.2f}.")
elif uf == 4:
    print(f"O valor final é {preço * 1.08:.2f}.")