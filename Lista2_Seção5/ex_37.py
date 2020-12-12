"""
Calculadora do valor de estacionamento, considerando
- Horas a pagar sempre inteiro e arredondando o excesso
- 1 e 2 hora R$ 1.00 cada
- 3 e 4 hora R$ 1.40 cada
- 5 em diante R$ 2.00 cada
- Intervalo entre chegada e partida não superior a 24 horas
"""

hora_entrada = input('Informe o horário de chegada (hh:mm:ss): ')

hora_saida = input('Informe o horário de partida (hh:mm:ss: ')

h1, m1, s1 = map(int, (hora_entrada.split(":")))
h2, m2, s2 = map(int, (hora_saida.split(":")))

if not(0 <= h1 <= 23):
    print('O horário de chegada apresenta erro nas horas.')
elif not (0 <= m1 <= 59):
    print('O horário de chegada apresenta erro nos minutos.')
elif not (0 <= s1 <= 59):
    print('O horário de chegada apresenta erro nos segundos.')
elif not(0 <= h2 <= 23):
    print('O horário de partida apresenta erro nas horas.')
elif not (0 <= m2 <= 59):
    print('O horário de partida apresenta erro nos minutos.')
elif not (0 <= s2 <= 59):
    print('O horário de chegada apresenta erro nos segundos.')

tempo_entrada = 0
tempo_entrada += int(hora_entrada.split(":")[0])*3600
tempo_entrada += int(hora_entrada.split(":")[1])*60
tempo_entrada += int(hora_entrada.split(":")[2])

tempo_saida = 0
tempo_saida += int(hora_saida.split(":")[0])*3600
tempo_saida += int(hora_saida.split(":")[1])*60
tempo_saida += int(hora_saida.split(":")[2])

tempo_total = tempo_saida - tempo_entrada

# 10000 / 60 / 60 = 2, porque fiz um casting para inteiro então não pega as casas decimais
hora_total = int(tempo_total / 60 / 60)
# 10000 - (2 * 60 * 60) = 2800
minuto_total = tempo_total - (hora_total * 60 * 60)
# 2800 / 60 =  46, porque fiz um casting para inteiro então não pega as casas decimais
minuto_total = int(minuto_total / 60)
# 10000 - (2 * 60 * 60) - (46 * 60) = 40
segundo_total = tempo_total - (hora_total * 60 * 60) - (minuto_total * 60)

# Se a soma do minuto incial com o minuto da duração for igual ou
# maior que 60, adiciona mais uma hora na hora final
if minuto_total >= 60:
    hora_total += 1
    minuto_total -= 60

# Se a soma do segundo incial com o segundo da duração for igual ou
# maior que 60, adiciona mais um minuto no minuto final
if segundo_total >= 60:
    minuto_total += 1
    segundo_total -= 60

if hora_total > 5:
    custo_total = ((2 * 1) + (2 * 1.4) + (2 * (hora_total - 4)))
elif 3 <= hora_total <= 4:
    custo_total = ((2 * 1) + (1.4 *(hora_total - 2)))
elif hora_total == 2:
    custo_total = 2
elif hora_total == 1:
    custo_total = 1

print(f"\nO tempo total de permanência foi de:\n"
      f"{hora_total}h {minuto_total}min {segundo_total}s \n"
      f"Com custo de R$ {custo_total:.2f}")