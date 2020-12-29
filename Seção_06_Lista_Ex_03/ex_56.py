"""
faça um programa que some todos os números primos abaixo de 2MM

Observações

1) Existe um teorema na matemática que diz que se um número não possui divisores até sua raiz quadrada então ele é primo, por isso o num**0.5

2) Este código supõe que o número n inserido será maior que 0, por isso a soma já começa = 2, uma vez que 2 é primo. E só passa a executar a verificação se n>1, caso contrário é impresso apenas 2.
"""

contador = 1
num = 3
soma = 2
referencia = 2000000

while num < referencia:
    primo = True
    verificador = 3
    while verificador <= num ** 0.5 and primo:
        if num % verificador == 0:
            primo = False
        verificador += 2
    if primo:
        contador += 1
        soma = soma + num
    num += 2
    # print(f"{num}", end=" ")
print(f'\n')
print(f"A soma dos {num} números primos é {soma}.")
