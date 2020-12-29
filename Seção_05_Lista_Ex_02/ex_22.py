"""
Em função da idade e do tempo de serviço valide se pode ou não
pedir aposentadoria
"""

print("Informe a idade e o tempo de serviço para saber \n"
      "se é possível pedir a aposentadoria.")

idade = int(input("Informe a idade:"))
ts = int(input("Informe o tempo de serviço:"))

if idade >= 65 or ts >= 30 or idade >= 60 and ts >= 25:
    print("Pedido de aposentadoria válido.")
else:
    print("Pedido inválido.")
