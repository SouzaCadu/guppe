"""
Sabendo o código do produto e quantidade, calcular o custo total
"""

print("Cardápio da lanchonete: \n"
      "Especificação   | Código | Preço \n"
      "Cachorro quente | 100    | 1.20 \n"
      "Bauru simples   | 101    | 1.30 \n"
      "Bauru com ovo   | 102    | 1.50 \n"
      "Hamburguer      | 103    | 1.20 \n"
      "Cheeseburguer   | 104    | 1.70 \n"
      "Suco            | 105    | 2.20 \n"
      "Refrigerante    | 106    | 1.00")
print()

cod = int(input("Digite o código do produto:"))

qtde = int(input("Digite a quantidade desejada:"))

print()
if cod == 100:
    print(f"O custo total é de R$ {qtde * 1.20:.2f}.")
elif cod == 101:
    print(f"O custo total é de R$ {qtde * 1.30:.2f}.")
elif cod == 102:
    print(f"O custo total é de R$ {qtde * 1.50:.2f}.")
elif cod == 103:
    print(f"O custo total é de R$ {qtde * 1.20:.2f}.")
elif cod == 104:
    print(f"O custo total é de R$ {qtde * 1.70:.2f}.")
elif cod == 105:
    print(f"O custo total é de R$ {qtde * 2.20:.2f}.")
elif cod == 106:
    print(f"O custo total é de R$ {qtde * 1.00:.2f}.")
else:
    print("Código inválido!")
