"""
Escrevendo em arquivos

Ao abrir um arquivo para leitura ele fica bloqueado para escrita, se aberto para a escrita o arquivo não pode ser
lido.

Abrindo um arquivo com o módulo "w", se o arquivo não existir ele será criado, caso exista será apagado e o conteúdo
será criado no novo arquivo.


with open("novo.txt", "w") as arquivo:
    arquivo.write("Podemos escrever qualquer conteúdo em um arquivo.\n")
    arquivo.write("Quando usamos a função write, o arquivo é criado automaticamente, caso não exista.\n")
    arquivo.write("Passaremos algumas linhas de texto.\n")
    arquivo.write("Para testar a função, usaremos sempre strings, pois do contrário teremos um erro.\n")

with open("novo.txt") as leitura:
    print(leitura.read())

Recebendo dados do usuário

with open("lista_compras.txt", "w") as lista_compras:
    while True:
        item = input("Insira um item da lista de compras ou digite sair: ")
        if item not in ("sair", "SAIR", "Sair"):
            lista_compras.write(item)
            lista_compras.write("\n")
        else:
            break
with open("lista_compras.txt") as lista_compras:
    print(lista_compras.read())

"""


