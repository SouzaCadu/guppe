"""
escreva um vetor que armazene 6 números inteiros:
- os valores são 1, 0, 5, -2, -5, 7
- armazene em uma variável o valor da soma das posições [0], [1], [5]
- modifique o valor na posição 4 para 100
- mostre na tela cada valor do vetor em um linha
"""

a = [1, 0, 5, -2, -5, 7]

soma = a[0] + a[1] + a[5]
print(soma)
print("---------")

a[4] = 100

for i in a:
    print(i)
