"""
22) Faça um programa que recebe como entrada o nome de um arquivo de entrada e o nome de um arquivo saída.
    O arquivo de entrada contém o nome de um aluno ocupando 40 caracteres e três inteiros que indicam suas notas.
    O programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde aparece o nome do aluno e as suas notas
    em ordem crescente.
"""


print("Informe o caminho do arquivo de entrada contendo o nome de cada aluno e suas três notas.\n"
      "A seguir informe o caminho do arquivo de saída, onde serão armazenados os dados em ordem crescente.")

import os

path1 = input("Informe o caminho do arquivo de entrada contendo o nome dos alunos e as notas: ")

while True:
    path2 = input("Informe o caminho do arquivo de saída onde serão salvos os dados ordenados: ")
    if os.path.isfile(path2):
        print("O arquivo já existe!")
    else:
        break


def organizar(dados):
    """
    Função que recebe uma lista no formato 'nome nota1 nota2 nota3' e retorna um map iterator
    com nota1, nota2 e nota3 em ordem crescente.
    :param dados: Arquivo contendo uma lista no formato 'nome nota1 nota2 nota3'
    :return: map iterator com nota1, nota2 e nota3 em ordem crescente.
    """
    alunos = [dado.split()[0] for dado in dados]
    notas = [[float(nota) for nota in dado.split()[1:]] for dado in dados]

    for nota in notas:
        if any(filter(lambda n: n > 10 or n < 0, nota)) or len(nota) != 3:
            raise ValueError()
        nota.sort()

    notas = [[str(n) for n in nota] for nota in notas]

    return map(lambda tupla: tupla[0] + ' ' + ' '.join(tupla[1]), zip(alunos, notas))


def gerar_notas(entrada, saida):
    """
    Função que recebe um arquivo como entrada com o nome do aluno e notas, e retorna as notas em ordem
    crescente em outro arquivo.
    :param entrada: Arquivo com as notas por aluno
    :param saida: Arquivo com as notas por aluno em ordem crescente
    :return: Notas por aluno em ordem crescente
    """

    try:
        with open(entrada) as arq_in:
            dados = arq_in.readlines()
    except (FileNotFoundError, OSError):
        return print('Arquivo inexistente. Favor conferir.')
    else:
        try:
            alunos_notas = organizar(dados)
        except (ValueError, IndexError):
            return print('Formato inválido')
        else:
            with open(saida, 'a') as arq_out:
                for aluno in alunos_notas:
                    arq_out.write(f'{aluno}\n')

            print('Concluído!')


gerar_notas(path1, path2)
