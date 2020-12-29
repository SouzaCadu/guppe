"""
se os números de 1 a 5 são escritos em palavras: um. dois, tres, quatro, cinco
então há 22 letras usadas no total.
faça um programa que conte quantas letras seriam
utilizadas se todos os números 1 a 1000 fossem
escritos em palavras, sem hífens ou espaços
"""

from num2words import num2words

letras = 0

for v in range(1, 1000 + 1):
    extenso = num2words(v, lang='pt-br')
    contagem = [x for x in extenso if x != ' ' or x != '-']
    letras += len(contagem)

print(f"Se tivessemos que escrever por extenso todos os números do 1 ao 1000,\n"
      f"utilizaríamos um total de {letras} letras.")