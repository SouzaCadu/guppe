"""
Dadas as operações fundamentais da matemática,
faça um programa que permita ao usuário escolher
a operação obter o resultado e voltar ao menu
"""

print("Selecione uma das opções para o cálculo das operações\n"
      "entre 2 números:\n"
      "1 - adição\n"
      "2 - subtração\n"
      "3 - multiplicação\n"
      "4 - divisão\n"
      "5 - saída")

opcao = int(input("Digite a opção desejada: "))

if opcao == 5:
    exit(print("Programa encerrado."))

if opcao not in (1, 2, 3, 4, 5):
    print("Opção inválida.")

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

if opcao == 4 and n2 == 0:
    print("Não existe divisão por zero.")
    n2 = float(input("Digite o segundo valor: "))

while True:
    if opcao == 1:
        print(f"O resultado da soma é {n1 + n2:.2f}")
    elif opcao == 2:
        print(f"O resultado da substração é {n1 - n2:.2f}")
    elif opcao == 3:
        print(f"O resultado da multiplicação é {n1 * n2:.2f}")
    elif opcao == 4:
        print(f"O resultado da divisão é {n1 / n2:.2f}")

    print("Selecione uma das opções para o cálculo das operações\n"
          "entre 2 números:\n"
          "1 - adição\n"
          "2 - subtração\n"
          "3 - multiplicação\n"
          "4 - divisão\n"
          "5 - saída")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 5:
        exit(print("Programa encerrado."))

    if opcao not in (1, 2, 3, 4, 5):
        print("Opção inválida.")

    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))

    if opcao == 4 and n2 == 0:
        print("Não existe divisão por zero.")
        n2 = float(input("Digite o segundo valor: "))
