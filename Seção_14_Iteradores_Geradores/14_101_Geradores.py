"""
Geradores

- Geradores (Generators) são iteradores (Iterators), nem todo um iterator é um generator.

Outras informações
- Generators podem ser criados com funções geradoras.
- Funções geradoras utilizam a palavra reservada yield.
- Generators podem ser criados com expressões geradoras.

Diferença entre funções e Generators Functions:

-----------------------------------------------------------------------------------------
/ Funções                               | Generator Functions                           /
-----------------------------------------------------------------------------------------
/ Utilizam return                       | utilizam yield                                /
-----------------------------------------------------------------------------------------
/ Retorna uma vez                       | podem utilizar yield múltiplas vezes          /
-----------------------------------------------------------------------------------------
/ Quando executada, retorna um valor    | quando executada retorna um generator         /
-----------------------------------------------------------------------------------------

# exemplo de Generator Function, não é um generator, ela gera um generator


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


gen = conta_ate(10)

print(gen, type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print("-----------------")
[print(i) for i in gen]

Uma vez que eu executo o generator ele executa e fica esperando o próximo next() por isso estão impressos os
primeiros 5 números linha a linha e o for imprime os demais

"""


