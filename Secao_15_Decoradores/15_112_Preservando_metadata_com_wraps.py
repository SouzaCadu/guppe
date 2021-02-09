"""
Preservando metadata com wraps

Metadata: São dados intrinsecos há um arquivo, que nem sempre são visualizáveis.

Wraps: São funções que envolvem elementos com diversas finalidades.

Função com problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu sou a função logar dentro de outra função#
        print(f"Você está utilizando a função {funcao.__name__}.")
        print(f"AQue possui a seguinte documentação {funcao.__doc__}.")
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    #Soma dois números#
        return a + b


# print(soma(10, 11))

print(soma.__name__, soma.__doc__)  # Manda o nome de logar e a documentação de logar

# Resolvendo o problema

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        #Eu sou a função logar dentro de outra função#
        print(f"Você está utilizando a função {funcao.__name__}.")
        print(f"AQue possui a seguinte documentação {funcao.__doc__}.")
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    #Soma dois números#
        return a + b


print(soma(10, 11))

print(soma.__name__, soma.__doc__)

"""


