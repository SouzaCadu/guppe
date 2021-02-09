"""
O que são Decorators

- São funções
- Decorators envolvem outras funções e aprimoram seus comportamentos
- Também são exemplos HOF
- Decorator tem uma sintaxe próprio, usando "@" (Syntatic Sugar)
- Decorator function é diferente do Decorator

# Decorators como função - Sintaxe não recomendada


def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer você")
        funcao()
        print("Tenha um ótimo dia")
    return sendo


def saudacao():
    print("Seja bem_vindo a Geek University")


# Testando 1
saudacao()  # Função comum
print("-" * 10)
teste = seja_educado(saudacao)
teste()  # Função decorada


# Testando 2


def raiva():
    print("EU TE ODEIO!!!!")

print("-" * 10)
raiva_educada = seja_educado(raiva)
raiva_educada()


# Decorators como função - Sintaxe recomendada


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("Foi um prazer conhecer você")
        funcao()
        print("Tenha um ótimo dia")
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print("Meu nome é Aaron")


# Testando
apresentando()

@seja_educado_mesmo
def dormir():
    print("Quero dormir!")

print("-" * 10)
dormir()


"""


