"""
faça um programa para ler a nota da prova de 15 alunos
e armazene num vetor, calcule e imprima a média geral
"""

print("Insira 15 notas para saber a média dos alunos.")

v1 = []
count = 1

while count <= 15:
    valor = int(input(f"Digite {count} de 15 notas: "))
    v1.append(valor)
    count += 1
    if count > 15:
        print(f"A média das notas é {sum(v1) / len(v1)}.")