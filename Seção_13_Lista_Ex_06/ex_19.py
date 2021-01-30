"""
19) Faça um programa que receba do usuário um arquivo que contenha o nome e a nota de diversos alunos.txt
    (da seguinte forma: NOME:JOÃO NOTA:8), um aluno por linha. Mostre na tela o nome e a nota do aluno que possui
    a maior nota.
"""

print("Informe um arquivo contendo uma relação de alunos e suas notas, ao final será exibido o nome do aluno\n"
      "com a maior nota.\n")

path = input("Digite o caminho de um arquivo contendo o nome dos alunos e as notas: ")


def maior_nota(path):
    """
    Recebe um arquivo contendo uma relação de alunos e suas notas e retorna o nome do aluno com a maior nota
    :param path: Caminho do arquivo contendo as informações
    :return: Nome do aluno com a maior nota
    """
    try:
        with open(path) as arquivo:
            alunos = arquivo.readlines()
        l_alunos = [(aluno.split(":")[1], float(aluno.split(":")[2])) for aluno in alunos]
        maior = max([aluno[1] for aluno in l_alunos])
        # retorna os dados do arquivo original, dada a condição de maior nota
        return ''.join(filter(lambda aluno: float(aluno.split(":")[2]) == maior, alunos))
    except FileNotFoundError:
        print("\nArquivo não encontrado!")
    except OSError:
        print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
    except ValueError:
        print("\nO modo que as informações se encontram no arquivo é inválido!")


print(f"O aluno com a maior nota é o {maior_nota(path)}!")
