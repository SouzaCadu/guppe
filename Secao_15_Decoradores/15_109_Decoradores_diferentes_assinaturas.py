"""
Decoradores com diferentes assinaturas

Relembrado Decorators

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f"Olá eu sou, {nome}!"


@gritar
def ordenar(principal, acompanhamento):
    return f"Olá eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor!"


print(saudacao("Charles Xavier"))
print(ordenar("Filé Oswaldo Aranha", "Salada"))


Para resolver o problema de assinaturas utilizamos o Decorator Pattern (*args, **kwargs). A assinatura de uma
função é representada pelo seu retorno, nome e parâmetros de entrada.

Utilizando Decorator Pattern podemos adicionar quantos parâmetros de entrada desejarmos. Podendo utilizar parâmetros
nomeados.

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f"Olá eu sou, {nome}!"


@gritar
def ordenar(principal, acompanhamento):
    return f"Olá eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor!"


print(saudacao("Tony Stark"))
print(ordenar("shawarma", "Salada grega"))
print(ordenar(principal="falafel", acompanhamento="tzatziki"))

Decorator com argumentos (parâmetro de entrada)

def verificar_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f"Valor incorreto, primeiro valor precisa ser igual a {valor}."
            return funcao(*args, **kwargs)
        return outra
    return interna


@verificar_primeiro_argumento("pizza")
def comida_favorita(*args):
    print(args)


@verificar_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# Testando


print(soma_dez(10, 12))  # 22
print(soma_dez(1, 21))  # Valor incorreto, primeiro valor precisa ser igual a 10.
print(comida_favorita("pizza", "churrasco"))
print(comida_favorita("sorve", "pizza"))


"""


