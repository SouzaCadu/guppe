"""
Manipulando data e hora

import datetime

print(dir(datetime))

print(datetime.MINYEAR, datetime.MAXYEAR)

print(datetime.datetime, datetime.datetime.now())  # <class 'datetime.datetime'>, 2021-02-12 19:12:35.202509

print(repr(datetime.datetime.now()))  # datetime.datetime(2021, 2, 12, 19, 13, 56, 852411)

inicio = datetime.datetime.now()

print(inicio)

# alterar o horário
inicio = inicio.replace(hour=20, minute=0, second=0, microsecond=0)

print(inicio)

# criando um evento
evento = datetime.datetime(2021, 2, 15, 0)

print(evento)
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.second)
print(evento.microsecond)

# data Python
nascimento = input("Informe sua data de nascimento no formato dd/mm/yy: ")

nascimento = nascimento.split("/")

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

"""
