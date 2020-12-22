"""
fazer um programa para ler 5 valores e, em seguida, mostrar a posição
onde se encontram o maior e o menor valor
"""

print("Insira 5 números para saber o maior, o menor e a posição que eles se encontram.")

v1 = []
count = 1

while count <= 5:
    valor = int(input(f"Digite {count} de 5 números: "))
    v1.append(valor)
    count += 1
    if count > 5:
        for i, j in enumerate(v1):
            if j == max(v1):
                indice1 = i
            if j == min(v1):
                indice2 = i
        print(f"O maior valor é {max(v1)} e a posição é {indice1} \n"
              f"e o menor valor é {min(v1)} e a posição é {indice2}.")
