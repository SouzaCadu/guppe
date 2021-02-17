"""
para representar um vetor de R³, implemente uma função que calcule a soma
de dois vetores. Essa função deve obedecer ao protótipo:
void soma (struct Vetor* v1, struct Vetor* v2, struct Vetor* res);
onde os parâmetros v1 e v2 são ponteiros para os vetores a serem somados, e o parâmetro
res é um ponteiro para uma estrutura vetor onde o resultado da operação deve ser
armazenado
"""


def soma(v1, v2, mult):
    """
    Função que recebe dois vetores e retorna outro vetor, com a soma dos elementos dos vetores
    recebidos por parâmetro
    :param v1: Recebe um vetor de números
    :param v2: Recebe um vetor de números
    :param mult: Vetor resultado da multiplicação v1 v2
    :return: Retorna um terceiro vetor com a soma dos elementos de cada vetor recebido. Caso
    os valores informados não sejam números, retorna um valor do tipo None
    """
    for i, z in zip(v1, v2):
        mult.append(i * z)
    return mult


vet1 = [2, 3, 5]
vet2 = [-3, 8, 9]
res = []
print(soma(vet1, vet2, res))
