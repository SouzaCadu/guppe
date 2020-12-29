"""
Faça um programa que leia vários números e calcule
 - a soma dos números digitados
 - a quantidade números digitados
 - a média dos números digitados
 - o maior número digitado
 - o menor número digitado
 - a média dos números pares
"""

lista = []
pares = []
contador = 0
num = int(input("Informe um numero: "))
while num != 0:
    lista.append(num)
    print(f"A soma dos numeros digitados é {sum(lista)}")
    print(f"A quantidade de numeros digitados foi {len(lista)}")
    print(f"A media dos números digitados foi {sum(lista) / len(lista):.2f}")
    print(f"O maior numero digitado foi {max(lista)}")
    print(f"O menor numero digitado foi {min(lista)}")
    if num % 2 == 0:
        pares.append(num)
        contador += 1
        print(f"A media dos numeros pares digitados é {sum(pares) / contador:.2f}")
    num = int(input("Informe um numero: "))
