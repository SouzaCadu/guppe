"""
faça um programa que leia uma matriz de 5 colunas e
4 colunas contendo as seguintes informações sobre
alunos de uma disciplina, sendo todas as informações do tipo
inteiro
- Primeira coluna: matrícula do aluno
- Segunda coluna: média das provas
- Terceira coluna: média dos trabalhos
- Quarta coluna: nota final
A - leia três primeiras informações de cada aluno
B - calcule a nota final como sendo a soma da média das provas
    e a média dos trabalhos
C - imprima a matrícula do aluno que obteve a maior nota
    final (assuma que só existe uma maior nota)
D - imprima a média aritmética das notas finais
"""

print("Insira as seguintes informações:\n"
      "Número da matrícula do aluno.\n"
      "Média das provas.\n"
      "Média dos trabalhos.\n"
      "A nota final será a média entre a média dos trabalhos e provas.")

info_alunos = ('Matrícula', 'Média provas', 'Média trabalhos')  # vetor para facilitar na hora do input

matriz = [[int(input(f'{info_alunos[i]}: ')) for i in range(3)] for _ in range(5)]  # preenchendo a matriz

for dados in matriz:  # inserindo a coluna das notas finais
    nota_final = (matriz[matriz.index(dados)][1] + matriz[matriz.index(dados)][2]) / 2  # média das notas de cada aluno
    dados.append(nota_final)

for linha in matriz:
    print(linha)

notas = [matriz[i][3] for i in range(5)]  # criando um vetor da última coluna
mat_maior_nota = matriz[notas.index(max(notas))][0]  # pegando a linha e a coluna da maior nota
media_notas = round(sum(notas) / 5, 3)  # média entre todas as notas

print(f'\nMatrícula do aluno com a maior nota: {mat_maior_nota}'
      f'\nMédia das notas {media_notas}')