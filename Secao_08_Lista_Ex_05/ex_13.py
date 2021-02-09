"""
faça uma função que receba dois valores numéricos e um símbolo que
represente a operação que se deseja efetuar com os números
"""


def opercao_aritmetica(n1, n2, operacao):
    """
    Recebe dois números reais e um símbolo representando uma
    das quatro operações elementares da matemática
    :param n1: Primeiro número
    :param n2: Segundo número
    :param operacao: Operação elementar da matemática + | - | / | *
    :return: a operação desejada entre os dois números informados
    """
    if operacao == "+":
        return n1 + n2
    elif operacao == "-":
        return n1 - n2
    elif operacao == "/":
        return f"{n1 / n2:.2f}"
    elif operacao == "*":
        return f"{n1 * n2:.2f}"


print(opercao_aritmetica(12.17, 98.78, "+"))
print(opercao_aritmetica(44, 15.35, "-"))
print(opercao_aritmetica(47589.18, 3698.98, "/"))
print(opercao_aritmetica(10.85, 78.98, "*"))
