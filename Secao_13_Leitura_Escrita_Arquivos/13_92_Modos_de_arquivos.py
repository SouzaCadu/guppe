"""
Modos de arquivos

r - abre o aquivo somente para leitura, por padrão
w - abre para escrita, sobrescrevendo o arquivo caso já exista
x - abre para escrita, somente se o arquivo não existir caso já exista retorna erro
a - abre para escrita, adiciona as informações ao final do arquivo caso ele já exista, se não existir ele cria o
    arquivo
+ - abre o arquivo para atualização, leitura e escrita

Obs. Para inserir o texto em outras posições do aquivo é necessário usar o comando seek(), usando a lógica do comando
readlines() podemos identificar quais são as posições das linhas e definir em que ponto colocar o cursor.


try:
    with open("novo.txt", "x") as arquivo:
        arquivo.write("Teste de conteúdo. \n")
except FileExistsError:
    print("Arquivo já existe.")


with open("lista_compras.txt", "a") as lista_compras:
    while True:
        item = input("Insira um item da lista de compras ou digite sair: ")
        if item not in ("sair", "SAIR", "Sair"):
            lista_compras.write(item)
            lista_compras.write("\n")
        else:
            break
with open("lista_compras.txt") as lista_compras:
    print(lista_compras.read())


with open("texto.txt", "r+") as arquivo:
    arquivo.seek()
    arquivo.write("Nova linha introdutória.")

with open("texto.txt") as arquivo:
    print(arquivo.read())

with open("texto.txt") as arquivo:
    print(len(arquivo.readlines()))

"""




