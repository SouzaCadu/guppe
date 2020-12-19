"""
Tuplas (tuples)

As tuplas são representadas por parênteses, são imutáveis toda a operação em uma
tupla gera uma nova tupla

Tuplas são definidas por vírgula e não por parênteses

print(type(()))

# Representações de uma tupla

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Tuplas podem ter apenas um elemento, a definição é em função da presença de vírgula

tupla3 = (3)
print(tupla3)
print(type(tupla3))

tupla4 = (3, )
print(tupla4)
print(type(tupla4))

# Gerando tuplas com função range

tupla5 = tuple(range(11))
print(tupla5, type(tupla5))

# Deseempacotar tuplas, sempre de tamanhos iguais var -> tupla

tupla6 = ("Geek University", "Programação em Python: Essencial")

escola, curso = tupla6

print(escola)
print(curso)

# Não existe método de adição e remoção de elementos para tuplas

# Soma, Máximo, Mínimo e Tamanho, apenas para valores inteiros ou reais

tupla7 = tuple(range(7))

print(sum(tupla7))
print(max(tupla7))
print(min(tupla7))
print(len(tupla7))

# Concatenar tuplas

tupla8 = (1, 2, 3, 4, 5)
tupla9 = (6, 7, 8, 9, 10)

print(tupla8)
print(tupla9)
print(tupla8 + tupla9)

tupla10 = tupla8 + tupla9

tupla8 += tupla9  # sobre escrevendo os valores de uma tupla

print(tupla8)

# Localizar elementos

print(3 in tupla8)

# Iterando sobre os elementos de uma tupla

for i in tupla8:
    print(i)

for indice, n in enumerate(tupla8):
    print(indice, n)

# Contando elementos em uma tupla

tupla11 = ("a", "a", "a", "b", "b", "c", "d", "e", "f")

print("a" in tupla11)
print(tupla11.count("b"))

tupla12 = tuple("Geek University")
print(tupla12.count("e"))

# Utilizando tuplas
# Sempre que os dados da coleção não precisam ser alterados

meses = ("Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez")

print(meses)
print(meses[2], meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Verificar em qual índice um elemento está localizado, se não existe retorna erro

print(meses.index("Ago"))

print(meses.index("Jun", 2))

# Slicing de tuplas[inicio:fim:passo]

print(meses[5:9])

# Por quê utilizar tuplas?

# São mais rápidas do que listas para processar
# Por serem imutáveis, são mais seguras

# Copiando uma tupla para outra, não há shallow copy

tupla13 = (1, 2, 3)
tupla14 = tupla13

print(tupla13)
print(tupla14)

tupla15 = (4, 5, 6)
tupla14 = (tupla14 + tupla15)

print(tupla15)
print(tupla14)

"""
