"""
Módulo Collections - Counter

Conhecido como High-performance Container Datetypes

Counter - recebe um iterável como parâmetro e cria u objeto do tipo counter collections,
assemelha-se ao um dicionário, contendo como chave o elemento da lista passada como parâmetro e
como valor a quantidade de ocorrências desse elemento.

"""
# Utilizando o Counter

from collections import Counter as counter

lista = [1, 2, 3, 4, 5, 8, 6, 6, 6, 6, 4, 4, 4, 8, 9, 9, 9, 0, 0, 0, 0, 10]
res = counter(lista)
print(res, type(res))

# Para cada elemento da lista o counter criou um valor (chave) e contou a quantidade de ocorrências

# Com strings, já que é um iterável
print(counter("Geek University: Programação em Python Essencial"))

# Com texto
texto = """
O que falta lembrar é que, de acordo com o pragmaticismo filosófico
de C. S. Peirce, crenças não ficam apenas depositadas em nossos 
pensamentos, mas são condutoras de nossas ações. 
Agimos de acordo com aquilo em que cremos. Pode-se tirar disso a lição
de que crenças precisam ser submetidas à autocrítica a qual deve 
resultar da capacidade de escuta e acatamento lúcido da heterocrítica.
"""
palavras = texto.split()
res1 = counter(palavras)
print(res1)
print(res1.most_common(5))
