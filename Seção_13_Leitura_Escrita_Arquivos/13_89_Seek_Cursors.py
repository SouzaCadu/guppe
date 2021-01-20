"""
Seek e Cursors

A função seek() é utilizada para movimentar o cursor pelo texto recebendo um parâmetro indicando onde queremos colocar
o cursor.

Outra forma de ler um arquivo é linha a linha com o comando readline.

Quando abrimos um arquivo é criada uma conexão entre o arquivo em disco e o programa. Ao finalizar o processamento
devemos fechar essa conexão com o comando close(). Podemos usar a função closed para verificar se um arquivo está
fechado ou aberto, esse comando retornará False se o arquivo estiver aberto e True se o arquivo estiver fechado.

arquivo = open("texto.txt")
print(arquivo.read())

arquivo.seek(90)
print(arquivo.read())

arquivo.seek(0)

retorno = arquivo.readline()
print(retorno, type(retorno))
print(retorno.split(' '))

arquivo.seek(0)

linhas = arquivo.readlines()
print(len(linhas))

print(arquivo.closed)
arquivo.close()
print(arquivo.closed)


"""
