"""
Levantando erros com Raise

Não é uma função, é uma palavra reservada. É útil para criarmos nossas próprias
exceções e mensagens de erro. Finaliza a função.

exemplo:

raise <TipoError>("Mensagem de erro")

def colore(texto, cor):
    cores = ("verde", "amarelo", "azul", "branco")
    if type(texto) is not str:
        raise TypeError("texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("cor precisa ser uma string")
    if cor not in cores:
        raise ValueError(f"A cor precisa ser um entre {cores}")
    return f"O texto {texto} ser impresso em {cor}."


print(colore("Geek", 7))
print(colore("Geek", "laranja"))


"""


