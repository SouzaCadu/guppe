"""
faça uma multiplicação e desconte 8% do total
"""

custo = 30
imposto = 0.08

print(f"O valor do dia trabalhado é de R$ {custo:.2f} . \n"
      f"Informe o número de dias trabalhados para saber o total \n"
      f"liquido de imppostos:")

dias = float(input())

print(f"O total a receber é de {(custo * dias) * (1-imposto)}.")