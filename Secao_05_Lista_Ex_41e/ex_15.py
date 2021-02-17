"""
Receba inteiros de 1 a 7 e exiba o dia da semana
começando no domingo
"""

dia = int(input("Informe o número para saber o dia da semana correspondente:"))

if 1 <= dia <= 7:
    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda-Feira")
    elif dia == 3:
        print("Terça-Feira")
    elif dia == 4:
        print("Quarta-Feira")
    elif dia == 5:
        print("Quinta-Feira")
    elif dia == 6:
        print("Sexta-Feira")
    else:
        print("Sábado")
else:
    print("Número inválido")
