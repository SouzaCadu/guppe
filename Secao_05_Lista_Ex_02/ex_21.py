"""
Monte um menu e execute a ação escolhida,
se a ação for inválida informe o erro.
"""

from sys import exit

print("Escolha a opção:"
      "1 - Soma de 2 números.\n"
      "2 - Diferença entre 2 números (maior pelo menor). \n"
      "3 - Produto entre 2 números. \n"
      "4 - Divisão entre 2 números (não há divisão por zero).")

opcao = int(input("Digite a opção desejada:"))

if opcao not in (1, 2, 3, 4):
    exit(print("Opção inválida!"))

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))

if opcao == 1:
    print(f"O resultado da soma é {n1 + n2:.2f}.")
elif opcao == 2:
    if n1 > n2:
        print(f"O resultado da subtração é {n1 - n2:.2f}.")
    else:
        print(f"O resultado da soma é {n2 - n1:.2f}.")
elif opcao == 3:
    print(f"O resultado da multiplicação é {n1 * n2:.2f}.")
elif opcao == 4:
    if n2 != 0:
        print(f"O resultado da divisão é {n1 /n2:.2f}.")
    else:
        print("Não existe divisão por zero!")

