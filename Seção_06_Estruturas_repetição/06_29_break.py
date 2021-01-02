"""
Saindo de loops com break

Utilizado para sair de loops de maneira projetada, criamos uma condição de parada para determinados loops




"""

# Exemplo 1

for numero in range(0, 150, 5):
    if numero == 75:
        break
    else:
        print(numero, end=" ")

# Exemplo 2
print()
while True:
    comando = input("Digite 'fim' para sair: ")
    if comando == 'fim':
        break