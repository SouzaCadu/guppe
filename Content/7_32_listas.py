"""
Listas

Funcionam como vetores ou matrizes, são dinamicos e permitem colocar qualquer tipo de dado

- Dinamico: Não possui tamanho fixo, podemos criar uma lista e adicionar elementos limitado
ao tamanho da memória disponível
- Qualquer tipo de dado: Não possuem tipo de dado fixo
- Aceitam repetições

As listas em Python são representadas por colchetes

lista1 = [1, 1, 1, 1, 1, 44, 99, 45, 67, 100, 12, 35, 2, 34.5, 3, 456, 4, 21, 22, 23, 24, 5, 6, 7, 112, 8, 112.3, 9,
          100]

lista2 = ["a", "b", "e", "f", "A", "S", "D", "F", "a", "b", "c"]

lista3 = []

lista4 = list(range(11))

lista5 = list("Geek University")

# Localizar termos

num = 9

if num in lista4:
    print(f"{num} está na lista 4")
else:
    print(f"{num} não está na lista 4")

# Ordenar os elementos

lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

# Contar os elementos

print(lista5.count("e"))
print(lista1.count(1))

# Adicionar elementos

print(lista3)
lista3.append(45)  # Um elemento por vez
print(lista3)

lista3.append([1, 2, 3, 4, 45, 46, 47, 49])
print(lista3)

if [1, 2, 3, 4, 45, 46, 47, 49] in lista3:
    print("Encontrei a lista.")
else:
    print("Não encontrei a lista.")

print(lista4)
lista4.extend([11, 12, 13])  # Adiciona elementos iteráveis, como, lista, string, termo a termo
print(lista4)

# Adicionar item de acordo com o índice, o item original será deslocado uma posição a direita

lista2.insert(2, "Novo valor")
print(lista2)

# Concatenando listas

lista6 = lista3 + lista4  # Assemelha-se ao extend
print(lista6)
lista3.extend(lista4)
print(lista3)

# Colocar os termos em ordem reversa

lista1.reverse()  # método built in
print(lista1)

print(lista1[::-1])  # slice de variável

# Copiar uma lista

lista7 = lista2.copy()

# Contar o total de elementos em uma lista

print(len(lista5))

# Remover o último termo de uma lista ou pelo índice

print(lista5)
lista5.pop()  # o pop remove e retorna o último elemento de uma lista
print(lista5)

print(lista2)
lista2.pop(3)  # os elementos a direita são deslocados a direita
print(lista2)

# Se não houver elemento no índice informado retornará um erro

# Zerar a lista

print(lista5)
lista5.clear()
print(lista5)

# Repetição de elementos em uma lista

print(lista2)
lista8 = lista2 * 2
print(lista8)

# Converter uma string em lista

curso = "Programação em Python: Essencial"
print(curso)
curso = curso.split()  # Por padrão separa por espaço
print(curso)

curso2 = "Programação,em,Python:,Essencial"
print(curso2)
curso2 = curso2.split(',')
print(curso2)

# Converter uma lista em string com qualquer tipo de separador

lista9 = ["Programação", "em", "Python:", "Essencial"]
curso3 = " ".join(lista9)
print(curso3)

curso4 = "#".join(lista9)
print(curso4)

# Iterando sobre uma lista

soma = ""
for i in lista8:
    print(i, end=" ")
    soma = soma + i
print(f"{soma}")

cesta = []
produto = []

while produto != "sair":
    print("Adicione um produto na lista ou sair para encerrar: ")
    produto = input()
    if produto != "sair":
        cesta.append(produto)

for produto in cesta:
    print(produto)

# Acessar os elementos de forma indexada / indexada inversa

cores = ["azul", "verde", "amarelo", "vermelho", "branco", "preto"]
print(cores[0])  # azul
print(cores[1])  # verde
print(cores[2])  # amarelo
print(cores[3])  # vermelho
print(cores[4])  # branco
print(cores[5])  # preto

print(cores[-1])  # preto
print(cores[-2])  # branco
print(cores[-3])  # vermelho
print(cores[-4])  # amarelo
print(cores[-5])  # verde
print(cores[-6])  # azul

# Revisão de loops

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Usando loops para gerar um índice

for indice, cor in enumerate(cores):
    print(indice, cor)

# Encontrar o índice de um elemento na lista

lista10 = [5, 6, 7, 8, 5, 9, 10]

print(lista10.index(6))

print(lista10.index(6))

print(lista10.index(5))  # vai retornar o indice do primeiro elemento encontrado

# O indice por ser usado referencia de busca, se não encontrar retornará erro
print(lista10.index(5, 2))  # busca o indice de 5 a partir da posição 2

print(lista10.index(5, 2, 6))  # busca o indice de 5 entre um intervalo

# Revisao slicing

# lista[inicio:fim:passo]
# podem ser usados valores negativos para inverter a ordem

lista11 = [1, 2, 3, 4]

print(lista11[::])  # todos os elementos

print(lista11[1:])  # do indice 1, inclusive, até o final

print(lista11[:3])  # de zero até o indice 3, exclusive

print(lista11[1:3])  # de 1 até 3, exclusive

print(lista11[1::2])  # de 1 até o final de 2 em 2

# Invertendo a posição dos itens na lista

lista11.reverse()
print(lista11)

# Soma, Máximo, Mínimo, Tamanho

print(sum(lista11))  # soma
print(max(lista11))  # máximo
print(min(lista11))  # mínimo
print(len(lista11))  # tamanho

# Converter lista em tupla

tupla11 = tuple(lista11)
print(tupla11)

# "Desempacotar" lista

n1, n2, n3, n4 = lista11
# Obs. se a qtde de variáveis e o tamanho da lista
# forem diferentes ocorrerá um erro

# Copiando uma lista para outra
# Deep copy e Shallow copy

# Deep copy

lista12 = [1, 2, 3]
print(lista12)

lista13 = lista12.copy()  # cria duas listas diferentes
print(lista13)
lista13.append(4)
print(lista12)
print(lista13)

# Shallow copy

lista14 = [4, 5, 6]
print(lista14)

lista15 = lista14  # cópia via atribuição
print(lista15)
lista14.append(7)
print(lista14)
print(lista15)

# Essa operação altera as duas listas
"""
