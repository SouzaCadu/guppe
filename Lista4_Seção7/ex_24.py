"""
faça um programa que leia 10 conjuntos de 2 valores
o primeiro representado o número do aluno e o segundo
sua altura em metros.
encontre o aluno mais baixo e o mais alto, mostre seus números e suas alturas
"""

print("Digite o código e a altura dos alunos para saber o maior e menor.")

cod_aluno = []
altura = []
count = 1

while count <= 10:
    cod_aluno.append(int(input("Digite o código do aluno: ")))
    altura.append(float(input("Digite a altura do aluno em metros: ")))
    count += 1

maior_aluno = max(altura)
cod_maior_aluno = altura.index(maior_aluno)

menor_aluno = max(altura)
cod_menor_aluno = altura.index(menor_aluno)

print(f"O maior aluno é {cod_maior_aluno} e tem {maior_aluno} metros \n"
      f"e menor aluno é {cod_menor_aluno} e tem {menor_aluno} metros.")
