"""
faça um programa que leia um valor N inteiro e positivo,
calcule e mostre o valor E, sendo:
- E = 1 + 1 / i! + ... + 1 / N!
"""

print("Insira um valor para receber a soma E = 1 + 1 / i! + ... + 1 / N!.")

n = int(input("Insira um número: "))

while n <= 0:
    n = int(input("Insira um número: "))

e = 0
fatorial = 1
count = 1

for i in range(n, 1, -1):
    while count <= n:
        fatorial *= count
        count += 1
        e = e + 1 / fatorial
print(f"A soma da série é {e:.2f}.")
