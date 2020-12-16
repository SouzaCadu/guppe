"""
Faça um algoritimo que converta a velocidade de km/h para m/s e vice versa
Crie um menu com duas opções de conversões e com uma opção para finalizar
O usuário poderá fazer quantas conversões desejar, finalize apenas na opção
do usuário
"""

print("Conversor de km/h para m/s:\n"
      "1 - de km/h para m/s\n"
      "2 - de m/s para km/h\n"
      "3 - para sair do programa.")

n = int(input("Digite a opção desejada: "))

if n == 1:
    kmh = float(input("Digite o valor em km/h: "))
    ms = kmh / 3.6
    print(f"O valor em m/s é {ms:.2f}.")

elif n == 2:
    ms = float(input("Digite o valor em m/s: "))
    kmh = ms * 3.6
    print(f"O valor em km/h é {kmh:.2f}.")

elif n == 3:
    print("Programa encerrado.")

while n != 3:
    n = int(input("Digite a opção desejada: "))

    if n == 1:
        kmh = float(input("Digite o valor em km/h: "))
        ms = kmh / 3.6
        print(f"O valor em m/s é {ms:.2f}.")

    elif n == 2:
        ms = float(input("Digite o valor em m/s: "))
        kmh = ms * 3.6
        print(f"O valor em km/h é {kmh:.2f}.")
    if n == 3:
        print("Programa encerrado.")
