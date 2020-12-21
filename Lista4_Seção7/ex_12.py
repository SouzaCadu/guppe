"""
faça um programa pra ler 5 valores e, em seguida, mostrar todos
os valores lidos, o maior, o menor e a média
"""

print("Insira 5 números reais para saber o maior, o menor e a média.")

v1 = []
count = 1

while count <= 5:
    valor = float(input(f"Digite {count} de 5 números: "))
    v1.append(valor)
    count += 1
    if count > 5:
        print(f"Os valores são {v1}, \n"
              f"o maior valor é {max(v1)}, \n"
              f"o menor valor é {min(v1)}, \n"
              f"e a média é  {sum(v1) / len(v1)}.")
