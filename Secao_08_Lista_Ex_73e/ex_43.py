"""
faça uma função que receba um vetor de inteiros e o preencha com
números aleatórios sem repetição
"""


def vetor_inteiros(lista):
    print("Informe números inteiros para serem adicionados a um vetor.\n"
          "Apenas serão aceitos elemento únicos.\n"
          "Para finalizar digite 'Sair'.")
    entrada = None
    conjunto = set({})
    while entrada != 'Sair':
        print('Digite aqui: ')
        entrada = input()
        if entrada in ("Sair", "sair", "SAIR"):
            break
        else:
            conjunto.add(int(entrada))
    return conjunto


lista = []
print(vetor_inteiros(lista))
