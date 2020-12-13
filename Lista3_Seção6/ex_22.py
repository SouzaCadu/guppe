"""
Faça um programa que permita ao usuário introduzir uma sequencia arbitrária de notas
válidas entre 10 e 20 e que mostre na tela o resultado correspondente a média
aritmética.
O número de notas não será fornecido ao programa, o programa
terminará quando for inserido um valor inválido
"""

print("Insira todas as notas para saber a média aritmética. \n"
      "Serão aceitos apenas valores entre 10 e 20,\n"
      "digite qualquer outro valor para saber a média.")

nota = int(input("Digite a nota ou 0 para saber a média: "))

notas = []

while 10 <= nota <= 20:
    notas.append(nota)
    nota = int(input("Digite a nota ou 0 para saber a média: "))
    if nota == 0:
        qtd = len(notas)
        soma = 0
        for valor in notas:
            soma = soma + valor
print(f"A média final é {soma / qtd:.2f}.")