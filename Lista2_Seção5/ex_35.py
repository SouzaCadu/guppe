"""
validador de datas
"""

print("Validador de datas. Digite os valores a seguir:")

dia = int(input("Digite o valor do dia:"))
mes = int(input("Digite o valor do mês:"))
ano = int(input("Digite o valor do ano (AAAA):"))

print()
if ano != 0:
    if mes in (1, 3, 5, 7, 8, 10, 12):
        if 1 <= dia <= 31:
            print("Data válida")
        else:
            print("Dia inválido")
    elif mes == 2:
        if (ano % 400 == 0) or ((ano % 4 == 0) and not (ano % 100 == 0)):
            if 1 <= dia <= 29:
                print("Data válida")
            else:
                print("Dia inválido")
    elif mes in (4, 6, 9, 11):
        if 1 <= dia <= 30:
            print("Data válida")
        else:
            print("Dia inválido")
    else:
        print("Mês inválido")
else:
    print("O ano não pode ser 0")
