"""
StringIO

Para ler ou escrever dados em um arquivo do sistema operacional, o software precisa ter permissão de leitura e escrita.

O StringIO é utilizado para a criação de arquivos em memória. Não faz parte das funções integradas do Python. Uma vez
que arquivo é criado a edição dele segue a mesma estrutura de comandos anteriores.

from io import StringIO

mensagem = "Essa é uma menagem de teste."
arquivo = StringIO(mensagem)
print(arquivo.read())

arquivo.write("\nNova linha de teste no arquivo em memória.")

arquivo.seek(0)

print(arquivo.read())

"""


