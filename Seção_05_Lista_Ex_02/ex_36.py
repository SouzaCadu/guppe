"""
Calculadora de comissão
"""

print("Calculadora de comissão:")
print()
valor_venda = float(input("Digite o valor da venda:"))

if valor_venda >= 100000:
    comissao = valor_venda * 0.16 + 700
    print(f"Valor da comissão é de R$ {comissao:.2f}")
elif 80000 <= valor_venda < 100000:
    comissao = valor_venda * 0.14 + 650
    print(f"Valor da comissão é de R$ {comissao:.2f}")
elif 60000 <= valor_venda < 80000:
    comissao = valor_venda * 0.14 + 600
    print(f"Valor da comissão é de R$ {comissao:.2f}")
elif 40000 <= valor_venda < 60000:
    comissao = valor_venda * 0.14 + 550
    print(f"Valor da comissão é de R$ {comissao:.2f}")
elif 20000 <= valor_venda < 40000:
    comissao = valor_venda * 0.14 + 500
    print(f"Valor da comissão é de R$ {comissao:.2f}")
elif valor_venda < 20000:
    comissao = valor_venda * 0.14 + 400
    print(f"Valor da comissão é de R$ {comissao:.2f}")
else:
    print("Valor inválido")
