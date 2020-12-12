"""
Leia o valor em reais e a cotaçao do dolar e retorne e o valor em dólares
"""

print(f"Conversor de reais em dólar. \n"
      f"Insira o valor em reais:")
r = float(input())

print(f"Insira a cotação do dólar:")
cd = float(input())

print(f"O valor em dólares é de USD{r * cd}.")