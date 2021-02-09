"""
Conjuntos

Referencia a teoria dos conjuntos da matemática.

Os conjuntos são chamados de set, em Python.
Não possuem valores duplicados, valores ordenados, não são indexados.

São úteis quando precisamos armazenar elementos quando não nos importamos com a
ordem, chaves, valores e itens duplicados.

Sets em Python são referenciados com chaves.

Diferentemente dos dicionários, os sets possuem apenas valor.

# Definindo um conjunto:

# Forma 1

s = set({1, 1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s, type(s))

# caso existam itens duplicados eles não serão adicionados

s1 = {1, 1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print(s1, type(s1))

# Iterando sobre set

for i in s1:
    if i == 3:
        print("Tem o 3.")
    else:
        print("Não é o 3.")

# Itens não ordenados

lista = [99, 2, 34, 2, 34, 23, 12, 1, 44, 5]
tupla = (99, 2, 34, 2, 34, 23, 12, 1, 44, 5)
dict1 = {}.fromkeys([1, 2, 3, 4, 5, 6], "Novo")
conjunto = set({99, 2, 34, 23, 12, 1, 44, 5})

print(f"Lista {lista} com {len(lista)} elementos")  # Aceita valores duplicados
print(f"Tupla {tupla} com {len(tupla)} elementos")  # Aceita valores duplicados
print(f"Dicionário {dict1} com {len(dict1)} elementos")  # Não aceita chaves duplicadas
print(f"Lista {conjunto} com {len(conjunto)} elementos")  # Não aceita valores duplicados

# Uso de sets

# Criar um conjunto de dados únicos, por exemplo, transformar uma lista com valores repetidos
# em um set que terá valores únicos

cidades = ["Campinas", "Campinas", "Fortaleza", "São Paulo", "Florianópolis", "Curitiba", "São Paulo"]
print(len(cidades))

set_cidades = set(cidades)
print(len(set_cidades))

# Adicionar elementos, duplicidade não gera erro, simplesmente é ignorado

set_cidades.add("Fortaleza")
print(set_cidades)
set_cidades.add("Porto Alegre")
print(set_cidades)

# Remover elementos 1, se não existir o elemento retorna um erro
set_cidades.remove("Porto Alegre")
print(set_cidades)

# Remover elementos 2, se não existir o elemento não retorna erro nem o elemento
set_cidades.discard("Campinas")
print(set_cidades)

# Deep copy

set_cidades1 = set_cidades.copy()
set_cidades1.add("Palmas")
print(f"{set_cidades} \n"
      f"{set_cidades1}")

# Shallow copy

set_cidades2 = set_cidades1
set_cidades2.add("Manaus")
print(f"{set_cidades2} \n"
      f"{set_cidades1}")

# Removendo elementos de um conjunto

set_cidades1.clear()
print(set_cidades1)

# Métodos matemáticos, dados 2 conjuntos:

estudantes_python = {"Marcos", "Patricia", "Felipe", "Augusto", "Luisa", "Ana", "Pedro", "Marcela"}
estudantes_java = {"Mariana", "Patricia", "Luiz", "Debora", "Tereza", "Ana", "Felipe"}

# União de conjuntos método 1
uniao = estudantes_python.union(estudantes_java)  # independemente da ordem o resultado é o mesmo
print(uniao)

# União de conjuntos método 2, com caracter PIPE " | "
pipe = estudantes_java | estudantes_python
print(pipe)

# Intersecção de conjuntos método 1
intersec = estudantes_python.intersection(estudantes_java)
print(intersec)

# Intersecção de conjuntos método 2 com &
intersec1 = estudantes_java & estudantes_python
print(intersec1)

# Diferença entre conjuntos
apenas_java = estudantes_java.difference(estudantes_python)
print(apenas_java)

apenas_python = estudantes_python.difference(estudantes_java)
print(apenas_python)

# Operações matemáticas, apenas com valores inteiros ou reais

inteiros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(sum(inteiros))
print(max(inteiros))
print(min(inteiros))
print(len(inteiros))

"""
