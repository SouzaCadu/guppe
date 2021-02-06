"""
Funções de maior grandeza - Higher Order Function - HOF

O que isso significa?
- Quando uma linguagem suporte HOF, ela permite que uma função receba outra função como argumento de entrada,
retorne outras funções como resultado e criar variáveis do tipo funções em nossos programas.

# Exemplos


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def dividir(a, b):
    return a / b


def multiplicar(a, b):
    return a * b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(4, 3, somar))
print(calcular(4, 3, subtrair))
print(calcular(4, 3, dividir))
print(calcular(4, 3, multiplicar))

Funções aninhadas - Nested Functions

Em Python podemos também ter funções de dentro da função, que são conhecidas como Nested Functions ou Inner Functions.
Podem acessar o escopo de funções mais externas.

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(("E aí ", "Suma daqui ", "Gosto muito de você "))
    return humor() + pessoa


print(cumprimento("Mark"))
print(cumprimento("Elon"))


def faz_me_rir():
    def rir():
        ha = "ha" * 10
        k = "kk" * 10
        lol = "lol" * 10
        return choice((ha, k, lol))
    return rir


# Testando

rindo = faz_me_rir()  # coloca a execução da função na variável rindo
print(rindo())  # coloca a variável para executar


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        ha = "ha" * 10
        k = "kk" * 10
        lol = "lol" * 10
        risada = choice((ha, k, lol))
        return f"{risada} {pessoa}"
    return dando_risada


# Testando
rindo = faz_me_rir_novamente("Charles")

print(rindo())
print(rindo())
print(rindo())

"""

