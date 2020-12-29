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

alunos = {cod_aluno[i]: altura[i] for i in range(0, len(cod_aluno))}

for chave, valor in alunos.items():
    if valor == alunos[max(alunos, key=alunos.get)]:
        print(f"O aluno mais alto é o código {chave} com {valor} metros de altura.")
    if valor == alunos[min(alunos, key=alunos.get)]:
        print(f"O aluno mais baixo é o código {chave} com {valor} metros de altura.")
