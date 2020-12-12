"""
Classificação do IMC
"""

print("Tabela de classificação do IMC:      \n"
      "IMC            | Classificação       \n"
      "< 18.5         | Abaixo do peso      \n"
      "18.6 - 24.9    | Saudável            \n"
      "25.0 - 29.9    | Excesso de peso     \n"
      "30.0 - 34.9    | Obesidade Grau I    \n"
      "35.0 - 39.9    | Obesidade Grau II   \n"
      ">= 40.0        | Obesidade Grau III    ")

peso = float(input("Informe o peso em kg:"))
altura = float(input("Informe a altura em metros:"))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f"IMC = {imc:.2f} Abaixo do peso.")
elif 18.5 < imc <= 24.9:
    print(f"IMC = {imc:.2f} Saudável.")
elif 25.0 <= imc <= 29.9:
    print(f"IMC = {imc:.2f} Excesso de peso.")
elif 30.0 <= imc <= 34.9:
    print(f"IMC = {imc:.2f} Obesidade Grau I.")
elif 35.0 <= imc <= 39.9:
    print(f"IMC = {imc:.2f} Obesidade Grau II.")
else:
    print(f"IMC = {imc:.2f} Obesidade Grau III.")
