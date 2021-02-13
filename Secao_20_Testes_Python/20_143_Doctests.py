"""
Doctests em Python

Para rodar um test do doctest:

python -m doctest -v nome_do_mobulo.py

Dentro do código replica o funcionamento do console Python

# Erro inesperado...

Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.


"""


def soma(a, b):
    """
    soma dois números
    :param a: qualquer número
    :param b: qualquer número
    :return: retorna a + b
    >>> soma(1, 2)
    3
    """
    return a + b


print(soma(3, 4))
