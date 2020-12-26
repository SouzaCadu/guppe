"""
faça um programa que leia duas matrizes 2 x 2
com valores reais e ofereça as seguintes opções:
- somar as duas matrizes
- subtrair a primeira da segunda
- adicionar uma constante às duas matrizes
- imprimir as matrizes
"""

soma = 0
matriz_soma = []
sub = 0
matriz_sub = []
matriz3 = []

valores = ('insira o valor', 'insira o valor')  # vetor para facilitar na hora do input

matriz1 = [[int(input(f'Matriz 1 {valores[i]}: ')) for i in range(2)] for _ in range(2)]  # preenchendo a matriz
matriz2 = [[int(input(f'Matriz 2 {valores[i]}: ')) for i in range(2)] for _ in range(2)]  # preenchendo a matriz

opcao = int(input(f"1 - Soma das matrizes: \n"
                  f"2 - Subtração da primeira matriz pela segunda: \n"
                  f"3 - Adicionar uma constante ãs duas matrizes: \n"
                  f"4 - Imprimir as matrizes: \n"
                  f"Selecione uma das opções:"))

if opcao == 1:
    for i in range(2):
        aux = []
        for j in range(2):
            soma = matriz1[i][j] + matriz2[i][j]
            aux.append(soma)
        matriz_soma.append(aux)
    print(f"A soma das matrizes é {matriz_soma}.")

if opcao == 2:
    for i in range(2):
        aux = []
        for j in range(2):
            sub = matriz1[i][j] - matriz2[i][j]
            aux.append(sub)
        matriz_sub.append(aux)
    print(f"A subtração das matrizes é {matriz_sub}.")

if opcao == 3:
    cte = int(input("Digite o valor da constante: "))
    for i in range(2):
        for j in range(2):
            matriz1[i][j] += cte
            matriz2[i][j] += cte
    print(f"As novas matrizes são {matriz1} e {matriz2} .")

if opcao == 4:
    print(f"As novas matrizes são {matriz1} e {matriz2} .")
