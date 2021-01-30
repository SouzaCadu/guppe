"""
20) Crie um programa que receba como entrada o número de alunos de uma disciplina. Aloque dinamicamente dois vetores
    para armazenar as informações a respeito desses alunos. O primeiro vetor contém o nome dos alunos e o segundo
    contém suas notas finais. Crie um arquivo que armazene, a cada linha, o nome do aluno e sua nota final.
    Use nomes com no máximo 40 caracteres. Se o nome não contém 40 caracteres, complete com espaço em branco.
"""

import os

path = os.path.abspath(os.getcwd())

nome = "notas_aluno.txt"

novo_arquivo = os.path.join(path, nome)

print("Informe a quantidade de registros que serão inseridos.\n"
      "A seguir entre com o nome e a nota de cada aluno.\n"
      "Os dados serão salvos notas_aluno.txt no mesmo diretório em que o programa estiver sendo executado.")

while True:
    try:
        num_alunos = int(input('Informe o número de alunos: '))
        break
    except ValueError:
        print('Valor invalido!')


alunos = []
notas = []
x = 1

while x < num_alunos + 1:
    aluno = input(f"Digite o nome do aluno {x} de {num_alunos}: ")
    try:
        nota = float(input(f"Digite a nota do aluno {aluno}: "))
    except ValueError:
        print('Valor invalido!')
    else:
        notas.append(nota)
    if len(aluno) > 40:
        print('Nome não pode ter mais que 40 caracteres!')
    else:
        y = 40 - len(aluno)
        aluno += " " * y
        alunos.append(aluno)
        x += 1

try:
    with open(novo_arquivo, 'w') as arq:
        for n in range(len(alunos)):
            arq.write(f'{alunos[n]}: {notas[n]}')
            arq.write('\n')
    print(f"Processo executado com sucesso em {path}/{nome}!")
    with open(novo_arquivo) as res:
        print(res.read())
except FileNotFoundError:
    print("\nArquivo não encontrado!")
except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")

