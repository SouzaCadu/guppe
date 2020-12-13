"""
escreva um algoritimo que leia certa quantidade de números e imprima o maior
deles e quantas vezes o maior número foi lido.
A quantidade de números a serem lidos deve ser fornecida
pelo usuário
"""

print("Digite quantos números desejar.\n"
      "Para saber qual o maior e quantas vezes ele foi digitado\n"
      "digite 0.")

maior = []
contador = []

n = int(input('Insira um número ou digite 0 para finalizar: '))

while n != 0:
    maior.append(n)
    contador = maior.count(max(maior))
    n = int(input('Insira um número ou digite 0 para finalizar: '))
print(f'O maior número foi {max(maior)}')
print(f'O maior número foi repetido {contador} vezes.')
