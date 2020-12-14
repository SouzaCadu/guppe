""""
faça um algorítimo que encontre o primeiro múltiplo de
11, 13 ou 17 após um número dado
"""

print("Vamos encontrar o primeiro múltiplo de 11, 13 ou 17 dado um número.")

n = int(input("Digite um número: "))

v1 = v2 = v3 = 0

for i in range(n, n+17):
    if i % 11 == 0:
        v1 = i
        break
    elif i % 13 == 0:
        v2 = i
        break
    elif i % 17 == 0:
        v3 = i
        break

if v1 != 0:
    print(f'O numero é divisivel por 11 e seu primeiro multiplo apos o {n} é: {v1}')
elif v2 != 0:
    print(f'O numero é divisivel por 13 e seu primeiro multiplo apos o {n} é: {v2}')
elif v3 != 0:
    print(f'O numero é divisivel por 17 e seu primeiro multiplo apos o {n} é: {v3}')
