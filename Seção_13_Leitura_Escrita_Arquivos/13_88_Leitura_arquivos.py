"""
Leitura de arquivos em Python

Para ler o conteúdo de um arquivo em Python, utilizamos função integrada open(). Na sua forma mais simples,
open recebe o caminho do arquivo a ser lido e retorno um objeto _io.TextIOWrapper, é com ele que trabalhamos.

Por padrão a função open abre o arquivo para leitura.

Após executar a abertura de arquivo o Python usa um recurso chamado cursor, um cursor marca o último ponto de execução
do código, ou seja, ele não processará novamente o comando já executado

A função read() lê todo o conteúdo do arquivo, linha a linha

arquivo = open("texto.txt")
print(arquivo, type(arquivo))

retorno = arquivo.read()
print(retorno, type(retorno))

"""

