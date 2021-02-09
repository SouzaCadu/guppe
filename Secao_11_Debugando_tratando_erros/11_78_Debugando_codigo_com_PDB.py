"""
Debugando erros

O debug é usado durante o desenvolvimento. O pdb é importado apenas nos pontos do código onde ele será utilizado,
pois ao final do debug ele será removido.

A partir do Python 3.7 o pdb passou a ser incorporada como função buil-in, breakpoint().

Caso dos nomes das variáveis sejam iguais aos nomes dos comandos do pdb, o acesso a elas deverá ser feito usando o
comando p para imprimir

Comandos do pdb:
l (lista onde estamos no código)
n (próxima linha)
p (imprime variável)
c (continua a execução - finaliza o debuging)


Com o Pycharm inserir pontos de parada:

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "O valor deve ser numérico."
    except ZeroDivisionError:
        return "Não é possível dividir por zero."


print(dividir(4, 0))

Nas versões < 3.7 do Python

nome = "Charles"
sobrenome = "Xavier"
import pdb; pdb.set_trace()
nome_completo = nome + " " + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + " " + "realizou o curso" + " " + curso
print(final)

Nas versões >= 3.7 do Python

nome = "Charles"
sobrenome = "Xavier"
breakpoint()
nome_completo = nome + " " + sobrenome
curso = "Programação em Python: Essencial"
final = nome_completo + " " + "realizou o curso" + " " + curso
print(final)

"""

