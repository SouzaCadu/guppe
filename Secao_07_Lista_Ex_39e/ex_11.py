"""
faça um programa que preencha um vetor com 10 números reais,
calcule e mostre a quantidade de números negativos e a soma
dos números positivos desse vetor
"""

print("Insira 10 números reais, positivos ou negativos, e saiba a soma desses valores.")

v1 = []
v2 = []
count = 1

while count <= 10:
    valor = float(input(f"Digite {count} de 10 números: "))
    if valor >= 0:
        v1.append(valor)
    else:
        v2.append(valor)
    count += 1
    if count > 10:
        print(f"A soma dos valore positivos {sum(v1)} \n"
              f"e a soma dos valore negativos {sum(v2)}.")
