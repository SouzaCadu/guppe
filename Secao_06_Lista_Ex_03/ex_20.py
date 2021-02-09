"""
ler uma sequencia de números inteiros e determinar se eles
são pares ou não.
- informe o número de valores lidos e números de pares
- o processo deve ser finalizado quando for digitado 1000
"""

contador_total = 0
contador_pares = 0

n = int(input("Digite um número ou 1000 para encerrar: "))

while n != 1000:
    contador_total += 1
    if n % 2 == 0:
        contador_pares += 1
    n = int(input("Digite um número ou 1000 para encerrar: "))
print(f"O total de números é {contador_total} e {contador_pares} são pares.")
