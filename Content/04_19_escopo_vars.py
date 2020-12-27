"""
Escopo de variáveis

Delimitação da variável

1 - Variáveis globais
São reconhecidas em todo o programa

2 - Variáveis locais
São reconhecidas apenas no bloco onde foram declaradas

Para declarar uma variável:
nome_da_variavel = valor_da_variavel
numero = 42

Python é uma linguagem dinamica, ao declarar uma variável
não declaramos o tipo
Este tipo é inferido ao atribuirmos o valor a mesma

# Tipagem dinamica
num = 42
print(num, type(num))

num = "Geek"
print(num, type(num))


# Diferença entre global e local
num = 42

if num > 10:
    novo = num + 10
    print(novo) # global, pq foi processada e pode ser acessada daqui em diante

print(novo, novo+10)

if num < 10:
    novo1 = num + 10
    print(novo1) # local pq não foi processada e não pode ser acessada pelo código

print(novo1, novo1+10)
"""
