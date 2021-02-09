"""
Entendendo o **kwargs

É mais um parâmetro, diferentemente do *args que coloca os valores como tupla,
o **kwargs exige que utilizemos parâmetros nomeados, transformado-os em
um dicionário

Nas nossas funções podemos ter parametros obrigatórios, *args, default e **kwargs
nessa ordem obrigatoriamente.

# Exemplos


def cores_favoritas(a, b, c, **kwargs):
    for pessoa, cor in kwargs.items():
        print(f"A cor favorita de {pessoa} é {cor}.")


cores_favoritas(1, 2, 3, Marcos="Verde", Julia="Branco", Fernanda="Roxo")


def cumprimento_especial(**kwargs):
    if "Geek" in kwargs and kwargs["Geek"] == "Python":
        return "Você recebeu um cumprimento Pythonico Geek"
    elif "Geek" in kwargs:
        return f"{kwargs['Geek']} Geek"
    return "Não tenho certeza de quem você é..."


print(cumprimento_especial())
print(cumprimento_especial(Geek="Python"))
print(cumprimento_especial(Geek="01"))
print(cumprimento_especial(Geek="Especial"))


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f"{nome} tem {idade} anos.")
    print(args)
    if solteiro:
        print("Solteiro")
    else:
        print("Casado")
    print(kwargs)


minha_funcao(18, "Ana")
minha_funcao(25, "Jones", 4, 5, 3, solteiro=False)
minha_funcao(39, "Bruce", eu="Não", você="Vai")
minha_funcao(45, "Charles", 9, 4, 3, java=False, pythpn=True)

# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Charles', 'sobrenome': 'Xavier'}
print(mostra_nomes(**nomes))


def somatorio(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)

somatorio(*lista)
somatorio(*tupla)
somatorio(*conjunto)
somatorio(**dicionario)

Os nomes da chave em um dicionário devem ser os mesmos
dos parâmetros da função


"""
