"""
21) Crie um programa que receba como entrada o número de alunos de uma disciplina. Aloque dinamicamente em uma
    estrutura para armazenar as informações a respeito desses alunos: nome do aluno e sua nota final. Use nomes com
    no máximo 40 caracteres. Em seguida, salve os dados dos alunos em um arquivo binário.
    Por fim, leia o arquivo e mostre o nome do aluno com a maior nota.
"""


import os

path = os.path.abspath(os.getcwd())

nome = "notas_aluno_binario.bin"

novo_arquivo = os.path.join(path, nome)

print("Informe a quantidade de registros que serão inseridos.\n"
      "A seguir entre com o nome e a nota de cada aluno.\n"
      "Os dados serão salvos notas_aluno_binario.bin no mesmo diretório em que o programa estiver sendo executado.")


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
    with open(novo_arquivo, 'ab') as arq:
        for n in range(len(alunos)):
            linha = f"{alunos[n]} {notas[n]}\n".encode("utf8")
            arq.write(linha)
    print(f"Processo executado com sucesso em {path}/{nome}!")
except FileNotFoundError:
    print("\nArquivo não encontrado!")
except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")

with open(novo_arquivo, "rb") as ler_arquivo:
    alunos = ler_arquivo.read().decode("utf8").splitlines()
    aluno = max(alunos, key=lambda dado: float(dado[41::]))
    print(f"\nO aluno com a maior nota é o {aluno[0:40:1]}")
