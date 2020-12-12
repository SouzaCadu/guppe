"""
Loop while serve para iterar sobre sequencias enquanto uma condição for verdadeira

while 'expressão booleana':
    // execução do loop

O bloco while será repetido enquanto a expressão booleana for verdadeira

# Exemplo 1

numero = 1

while numero < 1000:
    print(numero)
    numero += numero

# Exemplo 2

resposta = " "

while resposta != "sim":
    resposta = input("Já acabou? ")

Loop while necessita de uma condição de parada para que não se torne um loop infinito,
esse tipo de loop pode ser interessante em aplicações de jogos para atualização de telas ou
em robôs para que os sensores possam continuamente capturar dados do ambiente

"""