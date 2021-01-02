"""
Entendendo *args

é uma parâmetro de entrada especial de funções, pode ser chamado de
qualquer coisa desde que comece com um *, por convenção é utilizado *args

o parâmetros *args utilizado em uma função coloca os valores extras informadas
como entrada em uma tupla (que são imutáveis)


# Exemplo, transformando uma função simples


def soma_todos_numeros(n1, n2, n3):
    return n1 + n2 + n3


print(soma_todos_numeros(4, 5, 9))


def somatorio(*args):
    return sum(args)


print(somatorio())
print(somatorio(1))
print(somatorio(1, 2))
print(somatorio(1, 2, 3))
print(somatorio(1, 2, 3, 4))
print(somatorio(1, 2, 3, 4, -5, -8.9, 8, 10.5, 13.8))


def verifica_info(*args):
    if "Geek" in args and "University" in args:
        return "Bem vindo Geek!"
    return "Eu não tenho certeza de quem é você."


print(verifica_info())
print(verifica_info(1, True, "University", "Geek"))
print(verifica_info(1, "University", 3.14))


# Desempacotando listas


def somatorio(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]

print(somatorio(*numeros))
# Usando asteriscos informo ao Python que estamos passando uma coleção
# de dados, dessa forma ele precisará desempacotar os dados antes de fazer
# alguma operação


"""
