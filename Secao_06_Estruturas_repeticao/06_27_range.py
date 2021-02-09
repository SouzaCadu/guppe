"""
Ranges

Comando range gera um objeto range

- precisamos conhecer o loop for para usar ranges.
- precisamos conhecer o range para trabalhar melhor o loop for.

Range são utilizados para gerar sequencias numéricas, não aletórias, e especificadas

Formas gerais:

# Exemplo 1 (início padrão em 0, passo de 1 em 1)
for num in range(15):
    print(num, end="")

# Exemplo 2 (inicio especificado pelo usuário, passo de 1 em 1)
for num in range(4, 25):
    print(num, end="")

# Exemplo 3 (inicio determinado, passo especificado)
for num in range(5, 30, 3):
    print(num, end="")

# Exemplo 4 (valor inicio, valor de parada e passo) em ordem inversa
for num in range(10, -1, -1):
    print(num, end=" ")

"""