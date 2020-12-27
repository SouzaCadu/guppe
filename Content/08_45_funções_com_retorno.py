"""
Funções com retorno

São funções que retornam valores específicos
utiliza-se a palavra reservada return.

1 - return finaliza a função
2 - uma função pode ter vários return, porém retornará
    sempre o último
3 - podemos retornar qualquer tipo de dado ou múltiplos dados

O retorno de uma função pode ser combinado com outra
elemento do programa

# Exemplo


def quadro_7():
    return 7 ** 2


print(quadro_7())


# Refatorando Hello world


def hello_world():
    return "Hello World!"


print(hello_world()*3)


def hello_world():
    print("Executado antes do return...")
    return "Hello World!"


# funções com vários returns


def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return "b"


print(nova_funcao())


# retornando múltiplos valores


def outra_funcao():
    return 2, 3, 4, 5


n1, n2, n3, n4 = outra_funcao()
print(n1, n2, n3, n4)

print(outra_funcao(), type(outra_funcao()))


# Criando uma função para jogar uma moeda

from random import randint


def jogar_moeda():
    if randint(0, 1) == 0:
        return "Cara"
    return "Coroa"


print(jogar_moeda())

"""
