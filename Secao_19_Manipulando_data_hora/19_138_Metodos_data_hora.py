"""
Metodos

import datetime
from textblob import TextBlob

# aceita parâmetro de fuso horário (timezone)
agora = datetime.datetime.now()

print(type(agora), repr(agora), agora)

hoje = datetime.datetime.today()

print(type(hoje), repr(hoje), hoje)

# Mudanças acontecendo a meia noite
manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=3), datetime.time())

print(type(manutencao), repr(manutencao), manutencao)

# 0 - Monday
# 1 - Tuesday
# 2 - Wednesday
# 3 - Thursday
# 4 - Friday
# 5 - Saturday
# 6 - Sunday
print(manutencao.weekday())

nascimento = input("Informe sua data de nascimento no formato dd/mm/yyyy: ")

nascimento = nascimento.split("/")

aniversario = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em um sábado')
elif aniversario.weekday() == 6:
    print('Você nasceu em um domingo')


# formatando datas/horas com str(time) string format time
hoje = datetime.datetime.today()

hoje_formatado = hoje.strftime("%d/%m/%y")

print(hoje_formatado)


def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'


print(formata_data(hoje))

# Refatorando

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()

print(formata_data(hoje))

# utilizando o método strptime
nascimento = input("Informe sua data de nascimento no formato dd/mm/yyyy: ")

aniversario = datetime.datetime.strptime(nascimento, "%d/%m/%Y")

print(nascimento)

# horários
almoco = datetime.time(13, 10, 00)

print(almoco)

# Avaliando o tempo de processamento do código

import timeit, functools

# marcando o tempo de processamento de códigos

# Loop
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))

"""
