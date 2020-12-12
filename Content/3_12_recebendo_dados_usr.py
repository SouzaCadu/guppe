"""
recebendo dados do usuário
"""

""""
# Exemplo versão 2.x do Python

# Entrada de dados
print("Qual o seu nome?")
nome = input()

#Processamento

# Saída de dados
print("Seja bem-vindo(a) %s" % nome)

# Entrada de dados 2
print("Qual o seu nome?")
nome = input()
print("Seja bem-vindo(a) %s" % nome)

print("Qual a sua idade?")
idade = input()

print("%s, tem %s anos." % (nome, idade))
"""
""""
# Exemplo de print criado a partir das versões 3

# Input de dados
print("Qual o seu nome?")
nome = input()
print("Olá {0}, seja bem-vindo".format(nome))

print("Qual o seu nome?")
nome = input()

print("Qual a sua idade?")
idade = input()

print("Olá {0}, seja bem-vindo, você tem {1} anos".format(nome, idade))
"""

"""
# Exemplo mais moderno
print("Qual o seu nome?")
nome = input()
print(f"Seja bem-vindo(a) {nome}")

print("Qual o seu nome?")
nome = input()

print(f"Qual a sua idade {nome}?")
idade = input()

print(f"Olá {nome}, seja bem-vindo, você tem {idade} anos")
"""

"""
Em python tudo o que estiver entre
- aspas simple
- aspas duplas
- aspas simples triplas
- aspas duplas triplas
será considerado uma string

Todo o valor recebido via o comando input é uma string

cast --> converte um tipo de dado para outro
"""

# Versão otimizada do código
nome = input("Qual o seu nome?")
print(f"Seja bem-vindo(a) {nome}.")

idade = int(input(f"Qual a sua idade {nome}?"))
print(f"Olá {nome}, seja bem-vindo, você nasceu em {2020 - idade}.")