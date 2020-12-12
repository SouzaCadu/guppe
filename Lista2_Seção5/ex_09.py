"""
Se o valor calculado for maior que 20% do valor base
retorne "Empréstimo não concedido." do contrário
retonre "Empréstimo concedido."
"""

print("Validação do valor de parcela para liberação de empréstimo.")

sb = float(input("Insira o valor do salário base:"))

pmt = float(input("Insira o valor da parcela do empréstimo:"))

if pmt <= sb * 0.2:
    print("Empréstimo concedido.")
else:
    print("Empréstimo negado.")
