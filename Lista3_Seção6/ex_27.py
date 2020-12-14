"""
Faça um programa que leia um valor n inteiro e positivo
e apresente como sendo a soma da série harmônica
"""

print("Insira um valor para receber a soma da série harmônica.")

n = int(input("Insira um número: "))

while n < 0:
    n = int(input("Insira um número: "))

h = 0

for i in range(1, n+1):
    h = h + 1 / i
print(f"A soma da série harmônica é {h:.2f}.")
