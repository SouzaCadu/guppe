"""
faça um programa que leia um vetor de 5 posições para números reais, e depois,
um código inteiro.
Se 0 finaliza o programa, 1 mostra o vetor em ordem,
2 mostra o vetor em ordem inversa, se diferente informar que código inválido
"""

print("Insira 5 números.")

v1 = []
count = 1

while count <= 5:
    valor = int(input(f"Digite {count} de 5 números: "))
    v1.append(valor)
    count += 1
    if count > 5:
        codigo = int(input("Digite 0 para finalizar,\n"
                           "1 para ordem direta,\n"
                           "2 para ordem inversa: "))
        while codigo not in (0, 1, 2):
            print("Código inválido")
            codigo = int(input("Digite 0 para finalizar,\n"
                               "1 para ordem direta,\n"
                               "2 para ordem inversa: "))
        if codigo == 0:
            print("Programa finalizado.")
        elif codigo == 1:
            v1.sort()
            print(f"Lista em ordem direta {v1}.")
        elif codigo == 2:
            v1.reverse()
            print(f"Lista em ordem inversa {v1}.")

