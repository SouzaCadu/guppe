"""
escreva um programa que leia um número inteiro positivo N
e em seguida imprima N linhas do Triangula de Pascal
"""

def printPascal(n):
    # Iterate through every line
    # and print entries in it
    for line in range(0, n):
        # Every line has number of
        # integers equal to line
        # number
        for i in range(0, line + 1):
            print(binomialCoeff(line, i),
                  " ", end="")
        print()


def binomialCoeff(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)

    return res

n = int(input("Digite o número de linhas desejadas para o Triangulo de Pascal: "))
printPascal(n)
