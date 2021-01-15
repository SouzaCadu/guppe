"""
Bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no código.
Prevenindo que o programa pare de funcionar e o usuário receba a mensagem de
erro inesperado.

exemplo:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

# tratamento genérico (não recomendado)

try:
    geek()
except:
    print("Ocorreu algum problema com o código.")

try:
    len(5)
except:
    print("Ocorreu algum problema com o código.")

# tratamento específico

try:
    geek()
except NameError as err:
    print(f"Uso de função inexistente. {err}.")

try:
    len(5)
except TypeError as err:
    print(f"Uso de função inexistente. {err}.")

# tratamento de múltiplos erros

try:
    len(5)
except NameError as err_a:
    print(f"Ocorreu NameError {err_a}")
except TypeError as err_b:
    print(f"Ocorreu TypeError {err_b}")
except:
    print("Ocorreu um erro diferente.")

# uso em funções

def pega_valor(dic, chave):
    try:
        return dic[chave]
    except KeyError:
        return None


dic = {"nome": "Geek"}
print(pega_valor(dic, 8))

"""


